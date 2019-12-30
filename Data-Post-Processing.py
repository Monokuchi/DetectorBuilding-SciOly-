import numpy as np
import scipy
import time
import pdb
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt

def utcStrToDateNum(d):
    """@package docstring
    Converts a UTC string to a datatime object. Checks if input is already a datatime and just returns it.
    """
    d=d.decode("utf-8")
    if type(d) is datetime:
        return d
    else:
        # Converting UTC "yyyy-mm-dd hh:mm:ss.f" to datatime
        try:
            # Try parsing with fractional seconds
            dt = datetime.strptime(d, '%Y-%m-%d %H:%M:%S.%f')
        except ValueError as error:
            # We get here when no fractional seconds are present
            try:
                dt = datetime.strptime(d, '%Y-%m-%d %H:%M:%S')
            except ValueError as error:
                print("Unhandled time format:\n{}".format(error))
                return None
        return time.mktime(dt.timetuple()) + dt.microsecond*1e-6


t1, data1 = np.loadtxt(fname='C:\\Temp\\log.csv', delimiter=',', unpack=True, converters={0: utcStrToDateNum}, usecols=(0,1))
t2, data2 = np.loadtxt(fname='C:\\Temp\\loggerprolog.csv', delimiter=',', unpack=True, converters={0: utcStrToDateNum}, usecols=(0,1))

data2+=2


print(t1)

interpdata1= np.interp(t1, t1, data1)
interpdata2= np.interp(t1, t2, data2)

#FinalInterp=np.stack((interpdata1,interpdata2), axis=1)

#np.savetxt("C:\\Temp\\InterpolatedData.csv",FinalInterp,fmt="%f4",delimiter=",")

#Plotting
# plt.subplot(3,1,1)
# plt.plot(t1,data1)
# plt.subplot(3,1,2)
# plt.plot(t2)
# plt.subplot(3,1,3)
plt.scatter(interpdata1,interpdata2)
plt.show()

