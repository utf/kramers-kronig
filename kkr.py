# coding: utf-8

import numpy
def kkr(
        Energy :numpy.ndarray,
        Eps :numpy.ndarray,
        cshfit :float=10**-9,
        plot :bool=False
    ):
    Real = KKR_Real2Imag(Energy,
                         numpy.real(Eps),
                         cshfit,
                         plot)
    Imag = KKR_Imag2Real(Energy,
                         numpy.imag(Eps),
                         cshfit,
                         plot)
                      
def KKR_Real2Imag(
        Energy :numpy.ndarray,
        Eps :numpy.ndarray,
        cshfit :float=10**-9,
        plot :bool=False
        ):
    #falling Energy scale (eV, Hz) risign (nm)
    # care prefactor of integration substitude changing Energy units!
    if Energy[0] > Energy[1]:  #falling Energy scale
        Energy = numpy.flip(Energy)
        Eps = numpy.flip(Eps)
        Flip = True
    #interpolate equal spaced Energy grid
    Wi = numpy.linspace(min(Energy), max(Energy), len(Energy)*10) #fact 10 not nessary
    Eps_inter = numpy.interp(Wi , Energy, Eps)
    dE = Wi[1]- Wi[0]
    cshift = complex(0, dE * cshfit)
    Wi = numpy.array(Wi, dtype=numpy.complex128)
    #KramersKronig calculation based on code kkr from utf (Alex Ganose)
    def integration(w):
        factor = 1 / (Wi**2 -w**2 + cshift)
        KKR = numpy.sum((Eps_inter - 1) * factor )
        return(-2 * w / numpy.pi * dE * KKR )
    KKR_inter = numpy.real([integration(w) for w in Wi])
    #interpolate back to original Energy grid
    KKR = numpy.interp(Energy ,numpy.real(Wi), KKR_inter)
    if plot == True:
        plt.plot(Energy, Eps, ls='-', lw=4, label="Eps(Energy) Input data")
        plt.plot(Wi ,Eps_inter, ls=':', lw=3, label="Eps(Energy) interpolate @ space equal EnergyGrid")
        plt.plot(Wi ,KKR_inter, ls='-', lw=4, label="KKR of Eps(Energy) @ space equal EnergyGrid")
        plt.plot(Energy ,KKR, ls='--', lw=3, label="KKR of Eps(Energy) invers interpolateted @  Input EnergyGrid")
        plt.show()
    if Flip == True:
        KKR = numpy.flip(KKR)
    return(KKR)

def KKR_Imag2Real(
        Energy :numpy.ndarray,
        Eps :numpy.ndarray,
        cshfit :float=10**-9,
        plot :bool=False
        ):
    #falling Energy scale (eV, Hz) risign (nm)
    # care prefactor of integration substitude changing Energy units!
    if Energy[0] > Energy[1]: #falling Energy scale
        Energy = numpy.flip(Energy)
        Eps = numpy.flip(Eps)
        Flip = True
    #interpolate equal spaced Energy grid
    Wi = numpy.linspace(min(Energy), max(Energy), len(Energy)*10) #fact 10 not nessary
    Eps_inter = numpy.interp(Wi , Energy, Eps)
    dE = Wi[1]- Wi[0]
    cshift = complex(0, dE * cshfit)
    Wi = numpy.array(Wi, dtype=numpy.complex128)
    #KramersKronig calculation based on code kkr from utf (Alex Ganose)
    def integration(w):
        factor = Wi / (Wi**2 -w**2 + cshift)
        Integr = numpy.sum(Eps_inter * factor )
        return(1 + 2/numpy.pi * dE * Integr )
    KKR_inter = numpy.real([integration(w) for w in Wi])
    #interpolate back to original Energy grid
    KKR = numpy.interp(Energy ,numpy.real(Wi), KKR_inter)
    if plot == True:
        plt.plot(Energy, Eps, ls='-', lw=4, label="Eps(Energy) Input data")
        plt.plot(Wi ,Eps_inter, ls=':', lw=3, label="Eps(Energy) interpolate @ space equal EnergyGrid")
        plt.plot(Wi ,KKR_inter, ls='-', lw=4, label="KKR of Eps(Energy) @ space equal EnergyGrid")
        plt.plot(Energy ,KKR, ls='--', lw=3, label="KKR of Eps(Energy) invers interpolateted @  Input EnergyGrid")
        plt.show()
    if Flip == True:
        KKR = numpy.flip(KKR)
    return(KKR)

