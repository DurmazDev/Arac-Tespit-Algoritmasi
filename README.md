# Araç Tespit Algoritması
[Keras Retinanet](https://github.com/fizyr/keras-retinanet/) kullanılarak, Olasılık ve İstatistik dersi kapsamında oluşturulan "Araç Tespit Algoritması" kaynak kodları.

## Takım Üyeleri
<table>
    <tbody>
        <tr>
            <td align="center" valign="top" width="11.11%"><a href="https://github.com/barisazar"><img src="https://github.com/barisazar.png" width="100px;" alt="Baris Azar"/><br /><sub><b>Barış Azar</b></sub></a><br /><p>Üye</p></td>
            <td align="center" valign="top" width="11.11%"><a href="https://github.com/AAhmetDurmaz"><img src="https://github.com/AAhmetDurmaz.png" width="100px;" alt="A. Ahmet Durmaz"/><br /><sub><b>A. Ahmet Durmaz</b></sub></a><br /><p>Üye</p></td>
            <td align="center" valign="top" width="11.11%"><a href="https://github.com/YusufKizilgedik"><img src="https://github.com/YusufKizilgedik.png" width="100px;" alt="Yusuf Kızılgedik"/><br /><sub><b>Yusuf Kızılgedik</b></sub></a><br /><p>Üye</p></td>
        </tr>
    </tbody>
</table>

## Veri Seti
[NST-UYZ](https://github.com/AAhmetDurmaz/NST-UYZ) projesinde kullanılan NST-v3.3 veri setinin küçük bir kısmı seçilip sadece otomobil etiketleri kalacak şekilde düzenlenmiştir. Elde edilen veri seti, bu proje kapsamında [ResNet50](https://keras.io/api/applications/resnet/) modelinin eğitiminde kullanılacaktır. NST-v3.3 veri seti bir YOLO veri seti olduğundan dolayı "scripts" klasörü içerisinde bulunan Python scriptleri ile [PascalVOC](http://host.robots.ox.ac.uk/pascal/VOC/) tipine çevrilmiştir.

#### Örnek veri seti klasör yapısı:
```
└── dataset
    ├── Annotations
    │   ├── 1.xml
    │   ├── 2.xml
    │   └── ....
    ├── ImageSets
    │   └── Main
    │  	    ├── train.txt
    │  	    ├── val.txt
    │       └── test.txt
    └── JPEGImages
        ├── 1.jpg
        ├── 2.jpg
        └── ...
```

train.txt, test.txt ve val.txt içerisinde JPEGImages klasöründe bulunan verilerin isimleri yazmaktadır. Biz  tüm veri setinin %80'ini eğitim, geriye kalan %20'lik kısmı da test ve val için ayırdık.

Bu txt ayırımını otomatize eden dataset2txt.py kodu, scripts klasörü içerisinde bulunmakta.

## Eğitim
Keras Retinanet içerisinde bulunan train.py dosyası eğitimi kolayca yapabilmemize olana sağlıyor. Eğitim adımları detaylı olarak `ResNet50 Training with Keras-Retinanet.ipynb` not defterinde bulunmakta.

## Model ile tahmin yapma
Modelin eğitimi tamamlandıktan sonra scripts içerisindeki `predict.py` dosyası ile resimler üzerinde tahmin gerçekleştirilebilir.

Örnek kullanım:
```
python3 scripts/predict.py --input img1.jpg --output img1_output.jpg --backbone resnet50 --model ./resnet50_custom_trained.h5
```

### Örnek çıktılar:
<table>
  <tr>
    <th>Input</th>
    <th>Output</th>
  </tr>
  <tr>
    <td><img src="/src/inputs/1.jpg" alt="Resim 1"></td>
    <td><img src="/src/outputs/1_output.jpg" alt="Resim 1"></td>
  </tr>
  <tr>
    <td><img src="/src/inputs/2.jpg" alt="Resim 3"></td>
    <td><img src="/src/outputs/2_output.jpg" alt="Resim 3"></td>
  </tr>
  <tr>
    <td><img src="/src/inputs/3.jpg" alt="Resim 3"></td>
    <td><img src="/src/outputs/3_output.jpg" alt="Resim 3"></td>
  </tr>
  <tr>
    <td><img src="/src/inputs/4.jpg" alt="Resim 4"></td>
    <td><img src="/src/outputs/4_output.jpg" alt="Resim 4"></td>
  </tr>
</table>


## Lisans

Bu repo [MIT](https://choosealicense.com/licenses/mit/) lisansı ile lisanslanmıştır.
