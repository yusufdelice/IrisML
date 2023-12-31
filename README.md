# IrisML
https://irisml.onrender.com


Bu projede Python ve Python'un sklearn, streamlit, pandas, matplotlib ve seaborn kütüphaneleri kullanılmıştır. Ayrıca yapılan uygulama dockerize edilmeden internete sürülmüş ve bunun için; Github aracılığıyla Render hizmeti kullanılmıştır.
## Uygulama Detayları
Uygulama sklearn kütüphanesinde bulunan datasetlerden biri olan "iris"'i kullanır. Bu dataset'te Iris türüne ait 3 farklı çiçek çeşidini sepal ve taç yaprak uzunluklarına göre kaydedilmiştir. Sklearn diğer adıyla Scikit Learn, bir Makine Öğrenme kütüphanesidir ve içerisinde çeşitli Makine Öğrenimi işini kolaylaştıracak modeller bulunur. Bu modellerden Random Forest Classifier modelini kullanarak bir karar ağacı oluşturdum.
Streamlit kütüphanesini kullanarak kullanıcıdan aldığım değerlerle eğittiğim model için bir tahminde bulunmasını ve modelin bu tahmin için verdiği olasılığı, tahmin değeriyle birlikte ekrana basmasını sağladım.
Ayrıca eğitim verisetinde bulunan değerlerin bir özeti olması için her çiçek türünün özelliklerinin dağılımını gösteren küçük bir grafik hazırladım.

## İnternete Yüklemek
Ücretsiz bir seçeneği bulunan Render hizmeti, Github senkronizasyonu sayesinde projeleri direkt olarak kendi uzantısında bir siteye taşıyabiliyor. Bedava kullanımın kısıtlamaları yüzünden sitede yavaş yüklenme sıkıntıları olabilse de kod başarıyla çalışmakta.

## Ekran Görüntüleri
![image](https://github.com/yusufdelice/IrisML/assets/106596845/f716b074-7a93-4664-8045-9a44dcdf1ee1)
![image](https://github.com/yusufdelice/IrisML/assets/106596845/5a8226ef-b40a-4798-8d36-6a0e5c798900)
![image](https://github.com/yusufdelice/IrisML/assets/106596845/53b57984-282b-440c-a403-72327f28a99f)
