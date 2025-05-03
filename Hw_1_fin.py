from google.colab import files
uploaded = files.upload()
import pandas as pd
df = pd.read_csv('IMDB Dataset.csv')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Загрузка датасета
df = pd.read_csv('IMDB Dataset.csv')  

# Применение EDA
df['review_length'] = df['review'].apply(len)

# График 1: Распределение классов
plt.figure(figsize=(6, 4))
sns.countplot(x='sentiment', data=df)
plt.title('Распределение отзывов по классам')
plt.xlabel('Класс отзыва')
plt.ylabel('Количество')
plt.show()

# График 2: Распределение длины отзывов
plt.figure(figsize=(6, 4))
sns.histplot(df['review_length'], bins=50, kde=True)
plt.title('Распределение длины отзывов')
plt.xlabel('Длина отзыва (символы)')
plt.ylabel('Количество')
plt.show()


# финальный вариант