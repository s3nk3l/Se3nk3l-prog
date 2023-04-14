
print("Tere")

print()

auto_valik = input("Vali millist autot soovid Toyota, BMW, Audi, Rolls Royce, Tesla: ")
print()
laenutuse_aeg = int(input("Kui kauaks soovid autot (Päevades): "))

if laenutuse_aeg >= 3 and auto_valik == "Toyota":
    print("Toyota rent", laenutuse_aeg, "päevaks maksab",
          (laenutuse_aeg * 12)-(laenutuse_aeg * 12 * 0.1) + (laenutuse_aeg * 3), "eurot")
    print((laenutuse_aeg * 12)-(laenutuse_aeg * 12 * 0.1) + (laenutuse_aeg * 3), "€",
          " eurot on hind, sest Toyota maksab 12€ eurot päevas",
          "(", laenutuse_aeg * 12, "€ kokku", ")"
          "kuna auto on rentitud rohkem, kui 3 päevaks, tuleb lisada ka soodustus",
          "(", laenutuse_aeg * 12, "*", 0.1, ")", "see on nüüd", (laenutuse_aeg * 12) - (laenutuse_aeg * 12 * 0.1), "€")
    print("nüüd tuleb veel lisada kindlustus", "(", "3€ *", laenutuse_aeg, "päeva=", laenutuse_aeg*3, "€", ")",
          "nii, et kogu summa kokku on", (laenutuse_aeg * 12)-(laenutuse_aeg * 12 * 0.1) + (laenutuse_aeg * 3), "€")

elif laenutuse_aeg < 3 and auto_valik == "Toyota":
    print("Toyota rent", laenutuse_aeg, "päevaks maksab", (laenutuse_aeg * 12) + (laenutuse_aeg * 3), "€")
    print((laenutuse_aeg * 12) + (laenutuse_aeg * 3), "€ on hind, sest Toyota maksab 12€ päevas",
          "(", laenutuse_aeg * 12, "€", laenutuse_aeg, "päevaks", ")", "ja kindlustus maksab 3€ päevas, nii et", "(",
          laenutuse_aeg * 3, "€", laenutuse_aeg, "päeva eest", ")", "kõik kokku maksab",
          (laenutuse_aeg * 12), "+",  (laenutuse_aeg * 3), "=", (laenutuse_aeg * 12) + (laenutuse_aeg * 3), "€")


if laenutuse_aeg >= 3 and auto_valik == "BMW":
    print("BMW rent", laenutuse_aeg, "päevaks maksab",
          (laenutuse_aeg * 17)-(laenutuse_aeg * 17 * 0.12) + (laenutuse_aeg * 5), "eurot")
    print((laenutuse_aeg * 17)-(laenutuse_aeg * 17 * 0.12) + (laenutuse_aeg * 5), "€",
          " eurot on hind, sest BMW maksab 17€ eurot päevas",
          "(", laenutuse_aeg * 17, "€ kokku", ")"
          "kuna auto on rentitud rohkem, kui 3 päevaks, tuleb lisada ka soodustus",
          "(", laenutuse_aeg * 17, "*", 0.12, ")", "see on nüüd", (laenutuse_aeg * 17) - (laenutuse_aeg * 17 * 0.12))
    print("€", "nüüd tuleb veel lisada kindlustus", "(", "5€ *", laenutuse_aeg, "päeva=", laenutuse_aeg*5, "€", ")",
          "nii, et kogu summa kokku on", (laenutuse_aeg * 17)-(laenutuse_aeg * 17 * 0.12) + (laenutuse_aeg * 5), "€")

elif laenutuse_aeg < 3 and auto_valik == "BMW":
    print("BMW rent", laenutuse_aeg, "päevaks maksab", (laenutuse_aeg * 17) + (laenutuse_aeg * 5), "€")
    print((laenutuse_aeg * 17) + (laenutuse_aeg * 5), "€ on hind, sest BMW maksab 17€ päevas",
          "(", laenutuse_aeg * 17, "€", laenutuse_aeg, "päevaks", ")", "ja kindlustus maksab 5€ päevas, nii et", "(",
          laenutuse_aeg * 5, "€", laenutuse_aeg, "päeva eest", ")", "kõik kokku maksab",
          (laenutuse_aeg * 17), "+",  (laenutuse_aeg * 5), "=", (laenutuse_aeg * 17) + (laenutuse_aeg * 5), "€")


if laenutuse_aeg >= 3 and auto_valik == "Audi":
    print("Audi rent", laenutuse_aeg, "päevaks maksab",
          (laenutuse_aeg * 19)-(laenutuse_aeg * 19 * 0.15) + (laenutuse_aeg * 5), "eurot")
    print((laenutuse_aeg * 19)-(laenutuse_aeg * 19 * 0.15) + (laenutuse_aeg * 5), "€",
          " eurot on hind, sest Audi maksab 19€ eurot päevas",
          "(", laenutuse_aeg * 19, "€ kokku", ")"
          "kuna auto on rentitud rohkem, kui 3 päevaks, tuleb lisada ka soodustus",
          "(", laenutuse_aeg * 19, "*", 0.15, ")", "see on nüüd", (laenutuse_aeg * 19) - (laenutuse_aeg * 19 * 0.15))
    print("€", "nüüd tuleb veel lisada kindlustus", "(", "5€ *", laenutuse_aeg, "päeva=", laenutuse_aeg*5, "€", ")",
          "nii, et kogu summa kokku on", (laenutuse_aeg * 19)-(laenutuse_aeg * 19 * 0.15) + (laenutuse_aeg * 5), "€")


elif laenutuse_aeg < 3 and auto_valik == "Audi":
    print("Audi rent", laenutuse_aeg, "päevaks maksab", (laenutuse_aeg * 19) + (laenutuse_aeg * 5), "€")
    print((laenutuse_aeg * 19) + (laenutuse_aeg * 5), "€ on hind, sest BMW maksab 19€ päevas",
          "(", laenutuse_aeg * 19, "€", laenutuse_aeg, "päevaks", ")", "ja kindlustus maksab 5€ päevas, nii et", "(",
          laenutuse_aeg * 5, "€", laenutuse_aeg, "päeva eest", ")", "kõik kokku maksab",
          (laenutuse_aeg * 19), "+",  (laenutuse_aeg * 5), "=", (laenutuse_aeg * 19) + (laenutuse_aeg * 5), "€")


if laenutuse_aeg >= 3 and auto_valik == "Rolls Royce":
    print("Rolls Royce rent", laenutuse_aeg, "päevaks maksab",
          (laenutuse_aeg * 70)-(laenutuse_aeg * 70 * 0.03) + (laenutuse_aeg * 30), "eurot")
    print((laenutuse_aeg * 70)-(laenutuse_aeg * 70 * 0.03) + (laenutuse_aeg * 30), "€",
          " eurot on hind, sest Rolls Royce maksab 70€ eurot päevas",
          "(", laenutuse_aeg * 70, "€ kokku", ")"
          "kuna auto on rentitud rohkem, kui 3 päevaks, tuleb lisada ka soodustus",
          "(", laenutuse_aeg * 70, "*", 0.03, ")", "see on nüüd", (laenutuse_aeg * 70) - (laenutuse_aeg * 70 * 0.03))
    print("€", "nüüd tuleb veel lisada kindlustus", "(", "30€ *", laenutuse_aeg, "päeva=", laenutuse_aeg*30, "€", ")",
          "nii, et kogu summa kokku on", (laenutuse_aeg * 70)-(laenutuse_aeg * 70 * 0.03) + (laenutuse_aeg * 30), "€")


elif laenutuse_aeg < 3 and auto_valik == "Rolls Royce":
    print("Rolls Royce rent", laenutuse_aeg, "päevaks maksab", (laenutuse_aeg * 70) + (laenutuse_aeg * 30), "€")
    print((laenutuse_aeg * 70) + (laenutuse_aeg * 30), "€ on hind, sest Rolls Royce maksab 70€ päevas",
          "(", laenutuse_aeg * 70, "€", laenutuse_aeg, "päevaks", ")", "ja kindlustus maksab 30€ päevas, nii et", "(",
          laenutuse_aeg * 30, "€", laenutuse_aeg, "päeva eest", ")", "kõik kokku maksab",
          (laenutuse_aeg * 70), "+",  (laenutuse_aeg * 30), "=", (laenutuse_aeg * 70) + (laenutuse_aeg * 30), "€")

if laenutuse_aeg >= 3 and auto_valik == "Tesla":
    print("Tesla rent", laenutuse_aeg, "päevaks maksab",
          (laenutuse_aeg * 35)-(laenutuse_aeg * 35 * 0.2) + (laenutuse_aeg * 15), "eurot")
    print((laenutuse_aeg * 35)-(laenutuse_aeg * 35 * 0.2) + (laenutuse_aeg * 15), "€",
          " eurot on hind, sest Tesla maksab 35€ eurot päevas",
          "(", laenutuse_aeg * 35, "€ kokku", ")"
          "kuna auto on rentitud rohkem, kui 3 päevaks, tuleb lisada ka soodustus",
          "(", laenutuse_aeg * 35, "*", 0.2, ")", "see on nüüd", (laenutuse_aeg * 35) - (laenutuse_aeg * 35 * 0.2))
    print("€", "nüüd tuleb veel lisada kindlustus", "(", "15€ *", laenutuse_aeg, "päeva=", laenutuse_aeg * 15, "€", ")",
          "nii, et kogu summa kokku on", (laenutuse_aeg * 35)-(laenutuse_aeg * 35 * 0.2) + (laenutuse_aeg * 15), "€")


elif laenutuse_aeg < 3 and auto_valik == "Tesla":
    print("Tesla rent", laenutuse_aeg, "päevaks maksab", (laenutuse_aeg * 35) + (laenutuse_aeg * 15), "€")
    print((laenutuse_aeg * 35) + (laenutuse_aeg * 15), "€ on hind, sest Tesla maksab 35€ päevas",
          "(", laenutuse_aeg * 35, "€", laenutuse_aeg, "päevaks", ")", "ja kindlustus maksab 15€ päevas, nii et", "(",
          laenutuse_aeg * 15, "€", laenutuse_aeg, "päeva eest", ")", "kõik kokku maksab",
          (laenutuse_aeg * 35), "+",  (laenutuse_aeg * 15), "=", (laenutuse_aeg * 35) + (laenutuse_aeg * 15), "€")
