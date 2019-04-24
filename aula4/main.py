from lampada import Lampada

l1 = Lampada("led", 220, "branca", "volts", 27.9, "15W", "desligada")
l2 = Lampada("fluorescente", 110, "amarela", "revolt", 15, "27W", "desligada")


print(l1.getLampada())