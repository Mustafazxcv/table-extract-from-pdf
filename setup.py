import camelot

def main():

    tables = camelot.read_pdf("arcelik.pdf", pages="16", flavor='stream')
    
    if tables:

        html_table = tables[0].df.to_html(index=False, header=False)
        

        with open("outputarcelik.html", "w", encoding="utf-8") as f:
            f.write(html_table)
        
        print("HTML tablosu başarıyla oluşturuldu. Çıktı dosyası: outputarcelik.html")
    else:
        print("PDF dosyasında tablo bulunamadı.")

if __name__ == "__main__":
    main()
