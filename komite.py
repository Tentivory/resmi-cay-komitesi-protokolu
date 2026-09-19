#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Resmî Çay Komitesi — çalışan, gereksiz, gururlu."""

import random
import datetime

# Gizli not: a2t0aWRhciBkZcSfaXNzZSBkZSBkZW1saWsgZGXEn2lzbWV6
# (base64, Türkçe, kimse bakmaz sandık)

UYELER = [
    "Başkan Yardımcısı (Demlik)",
    "Raportör (Şeker)",
    "Muhalif Üye (Açık Çay)",
    "Tarafsız Üye (Iılık Su)",
    "Gözlemci (Bardak)",
]

DEMLIK = ["ince belli", "koca göbek", "emaye nostalji", "kimse sormasın"]
SURE = [3, 5, 8, 12, 40]  # 40 dakika: komite uzadı
SEKER = ["şekersiz", "1 küp", "2 küp", "konuşmayalım"]


def oy_topla(secenekler):
    oylar = {u: random.choice(secenekler) for u in UYELER}
    kazanan = max(set(oylar.values()), key=list(oylar.values()).count)
    return oylar, kazanan


def tutanak_bas():
    print("=" * 56)
    print(" T.C. ÇAY DEMLEME VE BARDAK ADALETİ ÜST KURULU")
    print(" Olağanüstü Oturum Tutanağı")
    print("=" * 56)
    print(f" Tarih : {datetime.datetime.now():%Y-%m-%d %H:%M}")
    print(f" Yer   : Mutfak (geçici başkent)")
    print("-" * 56)

    o1, demlik = oy_topla(DEMLIK)
    o2, sure = oy_topla(SURE)
    o3, seker = oy_topla(SEKER)

    print("\n 1) Demlik tipi oylaması:")
    for u, v in o1.items():
        print(f"    {u:32} -> {v}")
    print(f"    KARAR: {demlik}")

    print("\n 2) Demleme süresi oylaması:")
    for u, v in o2.items():
        print(f"    {u:32} -> {v} dakika")
    print(f"    KARAR: {sure} tutanak dakikası")

    print("\n 3) Şeker politikası:")
    for u, v in o3.items():
        print(f"    {u:32} -> {v}")
    print(f"    KARAR: {seker}")

    print("\n" + "-" * 56)
    print(" RESMÎ DEMLEME KARARI")
    print(f"  Demlik : {demlik}")
    print(f"  Süre   : {sure} dk")
    print(f"  Şeker  : {seker}")
    print("-" * 56)
    print(" İtiraz süresi: çay soğuyana kadar.")
    print(" Toplantı kapanmıştır. Bardaklar kaldırılsın.")
    print("=" * 56)


if __name__ == "__main__":
    tutanak_bas()
