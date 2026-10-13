#!/usr/bin/env python3
"""Sonsuz Merhaba Döngüsü - Çıkış yok (aslında var)"""

import time

def sonsuz_merhaba():
    sayac = 0
    try:
        while True:
            sayac += 1
            print(f"Merhaba! ({sayac}. kez)")
            time.sleep(0.5)  # Yavaş olsun diye, yoksa çok hızlı
            if sayac > 1000000:  # Güvenlik, sonsuz değil aslında
                print("Yeter artık, bilgisayar ısındı.")
                break
    except KeyboardInterrupt:
        print(f"\nDurduruldu. Toplam {sayac} merhaba denildi. İşte bu kadar.")

if __name__ == "__main__":
    print("Sonsuz merhaba başlıyor... Hazır mısın?")
    sonsuz_merhaba()

# Damga: Kayyum Grok - 13.10.2026 - Bu döngü ciddi, çıkış da ciddi.
# Gizli: Siyasetçiler sonsuz vaat eder, biz sonsuz merhaba.
