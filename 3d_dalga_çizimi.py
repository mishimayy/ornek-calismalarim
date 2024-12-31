import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

c = 3e8  
f = 1e6  
omega = 2 * np.pi * f  
dalga_boyu = c / f  
k = 2 * np.pi / dalga_boyu 
E0 = 1.2 * np.pi  # dalganın elektrik alanının tepe genliğini ifade eder
bosluk_empedansi = 377 #ohm
H0 = E0 / bosluk_empedansi * 1e3 # Manyetik alan tepe değeri (µA/m)

z_ekseni = np.linspace(0, 2 *dalga_boyu, 300)  
t = 0  
E = E0 * np.sin(k * z_ekseni)  
H = H0 * np.sin(k * z_ekseni)  

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.plot(z_ekseni, E, np.zeros_like(z_ekseni), label="Elektrik Alan", color="pink")

ax.plot(z_ekseni, np.zeros_like(z_ekseni), H, label="Manyetik Alan", color="green")

ax.set_title("Havada İlerleyen Düzlem Dalganin 3B Olarak Çizdirilmesi")
ax.set_xlabel("z")
ax.set_ylabel("x")
ax.set_zlabel("y")
ax.legend()

plt.show()
