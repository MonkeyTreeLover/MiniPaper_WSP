from astroquery.vizier import Vizier
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

#2013ApJ...767..120M, page 3, section 3

def ColorIndex(m1, m2, m3):
    return (m1-m2)-(m2-m3)



#vizier = Vizier() # this instantiates Vizier with its default parameters

################# NGC 6752 #################
NGC = Vizier(columns=["F275W", "F435W", "F336W", "Teffspectro"])
NGC.ROW_LIMIT = 250

catalog = NGC.get_catalogs('J/A+A/677/A86/tableb5')[0]

xNGC6752 = np.array(catalog["F275W"]-catalog["F435W"])
yNGC6752 = ColorIndex(catalog["F275W"], catalog["F336W"], catalog["F435W"]) #

plt.scatter(xNGC6752, yNGC6752, c=catalog["Teffspectro"]/1e3, cmap="gist_rainbow", s=10)
plt.colorbar(label="Teff (kK)")

plt.text(-2.3, -0.25, "NGC 6752")

# M jump
rect = plt.Rectangle((-1.3, 1.2), 0.2, -1.62, color="gray", alpha=0.5)
plt.gca().add_patch(rect)

plt.text(-1.2, -0.25, "M",)
plt.text(-1.2, 1, r"$18.4 \pm 1.3$kK", fontsize=8)


# G jump
rect = plt.Rectangle((-0.3, 1.2), 0.2, -1.62, color="gray", alpha=0.5)
plt.gca().add_patch(rect)

plt.text(-0.2, -0.25, "G",)
plt.text(-0.2, 1, r"$11.2 \pm 0.2$kK", fontsize=8)

# Properties of the plot
plt.xlabel("F275W-F435W")
plt.ylabel(r"$C_{F275W,F336W,F435}$")

plt.xlim(-2.5, 1.3)
plt.ylim(-0.4, 1.2)

plt.gca().invert_yaxis()

plt.savefig(r"Pictures\NGC6752.png")
plt.show()

################# omega Centauri #################
wCen = Vizier(columns=["F275W", "F438W", "F336W", "Teffspectro"])
wCen.ROW_LIMIT = 250

catalog = wCen.get_catalogs('J/A+A/677/A86/tableb6')[0]

xwCen = np.array(catalog["F275W"]-catalog["F438W"])
ywCen = ColorIndex(catalog["F275W"], catalog["F336W"], catalog["F438W"]) #

plt.scatter(xwCen, ywCen, c=catalog["Teffspectro"]/1e3, cmap="gist_rainbow", s=10)
plt.colorbar(label="Teff (kK)")

plt.text(-2.3, -0.25, r"$\omega$ Cen")

# M jump
rect = plt.Rectangle((-1.3, 1.2), 0.2, -1.62, color="gray", alpha=0.5)
plt.gca().add_patch(rect)

plt.text(-1.2, -0.25, "M",)
plt.text(-1.2, 1, r"$18.4 \pm 2.2$kK", fontsize=8)


# G jump
rect = plt.Rectangle((-0.3, 1.2), 0.2, -1.62, color="gray", alpha=0.5)
plt.gca().add_patch(rect)

plt.text(-0.3, -0.25, "G",)
plt.text(-0.2, 1, r"$11.2 \pm 0.3$kK", fontsize=8)

# Properties of the plot
plt.xlabel("F275W-F438W")
plt.ylabel(r"$C_{F275W,F336W,F438}$")

plt.xlim(-2.5, 1.3)
plt.ylim(-0.4, 1.2)

plt.gca().invert_yaxis()

plt.savefig(r"Pictures\wCen.png")
plt.show()