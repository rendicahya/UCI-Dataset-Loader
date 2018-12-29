import numpy as np
import pandas as pd


def iris():
    path = 'datasets/iris.csv'
    names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'label']
    df = pd.read_csv(path, names=names, index_col=False)
    df = df.replace(['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'], [0, 1, 2]).values
    X = df[:, :4].astype(np.float16)
    y = df[:, 4].astype(np.uint8)

    return X, y


def adult():
    path = 'datasets/adult.csv'
    names = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship',
             'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'label']
    df = pd.read_csv(path, names=names, index_col=False)
    df = df.applymap(lambda x: x.strip() if type(x) is str else x)

    for col in df:
        if df[col].dtype == 'object':
            df = df[df[col] != '?']

    replace = [
        ['Private', 'Self-emp-not-inc', 'Self-emp-inc', 'Federal-gov', 'Local-gov', 'State-gov', 'Without-pay',
         'Never-worked'],
        ['Bachelors', 'Some-college', '11th', 'HS-grad', 'Prof-school', 'Assoc-acdm', 'Assoc-voc', '9th', '7th-8th',
         '12th', 'Masters', '1st-4th', '10th', 'Doctorate', '5th-6th', 'Preschool'],
        ['Married-civ-spouse', 'Divorced', 'Never-married', 'Separated', 'Widowed', 'Married-spouse-absent',
         'Married-AF-spouse'],
        ['Tech-support', 'Craft-repair', 'Other-service', 'Sales', 'Exec-managerial', 'Prof-specialty',
         'Handlers-cleaners', 'Machine-op-inspct', 'Adm-clerical', 'Farming-fishing', 'Transport-moving',
         'Priv-house-serv', 'Protective-serv', 'Armed-Forces'],
        ['Wife', 'Own-child', 'Husband', 'Not-in-family', 'Other-relative', 'Unmarried'],
        ['White', 'Asian-Pac-Islander', 'Amer-Indian-Eskimo', 'Other', 'Black'],
        ['Female', 'Male'],
        ['United-States', 'Cambodia', 'England', 'Puerto-Rico', 'Canada', 'Germany', 'Outlying-US(Guam-USVI-etc)',
         'India', 'Japan', 'Greece', 'South', 'China', 'Cuba', 'Iran', 'Honduras', 'Philippines', 'Italy', 'Poland',
         'Jamaica', 'Vietnam', 'Mexico', 'Portugal', 'Ireland', 'France', 'Dominican-Republic', 'Laos', 'Ecuador',
         'Taiwan', 'Haiti', 'Columbia', 'Hungary', 'Guatemala', 'Nicaragua', 'Scotland', 'Thailand', 'Yugoslavia',
         'El-Salvador', 'Trinadad&Tobago', 'Peru', 'Hong', 'Holand-Netherlands'],
        ['>50K', '<=50K']
    ]

    for row in replace:
        df = df.replace(row, range(len(row)))

    df = df.values
    X = df[:, :14].astype(np.uint32)
    y = df[:, 14].astype(np.uint8)

    return X, y


def wine():
    path = 'datasets/wine.csv'
    names = ['label', 'Alcohol', 'Malic acid', 'Ash', 'Alcalinity of ash', 'Magnesium', 'Total phenols', 'Flavanoids',
             'Nonflavanoid phenols', 'Proanthocyanins', 'Color intensity', 'Hue', 'OD280/OD315 of diluted wines',
             'Proline']
    df = pd.read_csv(path, names=names, index_col=False).values
    X = df[:, 1:].astype(np.float16)
    y = df[:, 0].astype(np.uint8)

    return X, y


def car_eval():
    path = 'datasets/car_eval.csv'
    names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'label']
    df = pd.read_csv(path, names=names, index_col=False)
    replace = [
        ['low', 'med', 'high', 'vhigh'],
        ['small', 'med', 'big'],
        ['low', 'med', 'high'],
        ['unacc', 'acc', 'good', 'vgood']
    ]

    for row in replace:
        df = df.replace(row, range(len(row)))

    df = df.replace({'doors': {'5more': 5}, 'persons': {'more': 6}})
    df.doors = df.doors.apply(lambda x: int(x) - 2)
    df.persons = df.persons.apply(lambda x: (int(x) // 2) - 1)
    df = df.values.astype(np.uint8)
    X = df[:, :6]
    y = df[:, 6]

    return X, y
