# streamlit, pandas ve hem model hem dataset için yararlanacağımız sklearn kütüphanelerini import ediyoruz.
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns

# sayfaya bir başlık ve açıklama ekliyoruz.
st.write("""
# Çiçek Türü Tahmin Etme Uygulaması

Bu uygulama sklearn kütüphanesinde native olarak bulunan, R.A. Fisher tarafından 1988 yılında oluşturulmuş 'iris' verisetini kullanır. Kullanıcıdan alınan değerlerin, mevzu bahis iris familyasına ait üç ayrı çiçek çeşidi arasından hangi türe daha yakın olduğuna dair bir tahmin oluşturur.
""")
st.write("Sayfanın aşağısına inerseniz, verinin değerler için görselleştirilmiş bir halini bulabilirsiniz.")
st.write("-Yusuf Talha DELİCE")
# ekranda kütüphaneler yüzünden çıkabilecek uyarıları engelliyorum.
st.set_option('deprecation.showPyplotGlobalUse', False)

# bir sidebar, yani yan pencere oluşturuyoruz, kullanıcı buradan özellikleri seçecek ve model hangi çiçeğe daha yakın olduğuna dair tahmin yürütecek.
st.sidebar.header('Kullanıcı Girdisi')

# kullanıcıdan değerlerin alınacağı fonksiyon.
def user_input_features():
    sepal_length = st.sidebar.slider('Sepal uzunluğu', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal genişliği', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Taç yaprağı uzunluğu', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Taç yaprağı genişliği', 0.1, 2.5, 0.2)
    data = {'sepal uzunluğu': sepal_length,
            'sepal genişliği': sepal_width,
            'petal uzunluğu': petal_length,
            'petal genişliği' : petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

# alınan değerler için bir dataframe oluşturuyorum.
df = user_input_features()

# alınan değerleri basıyorum.
st.subheader('Kullanıcı Girdisi')
st.write(df)

# sklearn kütüphanesinde bulunan datasetlerden biri olan iris'i kullanıyorum.
iris = datasets.load_iris()
X = iris.data
y = iris.target

# model olarak random forest classifier'ı seçiyorum.
clf = RandomForestClassifier()
clf.fit(X, y)

# tahmin değerini ve model'in bu tahmin için sklearn'ın tekrar içerisinde bulunan ve ağaç sistemlerinde güven ortalamasını alarak bulduğu olasılık değerini bastırıyorum.
prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Çiçek Türleri')
st.write(iris.target_names)

st.subheader('Tahmin')
st.write(iris.target_names[prediction])
#st.write(prediction)

st.subheader('Tahmin Olasılığı')
st.write(prediction_proba)

# eğitimde kullanılan verinin tamamını ve çiçeklerin verilen feature'lara göre bir grafiğini bastırıyorum.
st.subheader("Eğitimde Kullanılan Tüm Veri")
#st.write(type(iris.data))
X = pd.DataFrame(iris.data)
y = pd.DataFrame(iris.target)
data = pd.merge(X,y, left_index=True, right_index=True)
data.columns = ['sepal_uzunluk', 'sepal_genislik', 'tac_yaprak_uzunluk', 'tac_yaprak_genislik', 'cicek_turu']
data


st.subheader("Verinin Görselleştirilmiş Hali")
plt.figure(figsize=(10, 8))

plt.subplot(2,2,1)
sns.violinplot(x='cicek_turu', y='sepal_uzunluk', data=data)
plt.subplot(2,2,2)
sns.violinplot(x='cicek_turu', y='sepal_genislik', data=data)
plt.subplot(2,2,3)
sns.violinplot(x='cicek_turu', y='tac_yaprak_uzunluk', data=data)
plt.subplot(2,2,4)
sns.violinplot(x='cicek_turu', y='tac_yaprak_genislik', data=data)
plt.tight_layout()
st.pyplot()
