import json
import pandas as pd
import pickle as pk
from models import models

# метрики моделей
# from score import __all__, CA
# metrics = {m: None for m in __all__}


def models_calc(x):
    # global models, metrics
    # инициализация моделей
    for m, val in models.items():
        with open(models[m]['passport']['model_filename'], mode='rb') as file:
            models[m]['model'] = pk.load(file)
            print(f'{m}.domain: {models[m]["model"].domain}')

        # обработка csv-файла
        with open(models[m]['passport']['train_dataset_filename'], newline='') as file:
            data = pd.read_csv(file)
            # print(data.head(0), data.loc[4], data.loc[17], data.loc[49])

    # Конвертация входных данных
    # x = data.iloc[7, :4]
    # результат вычисления моделей
    y = {}
    metrics = {}
    for name, val in models.items():
        print(f'x = {x}')
        m = models[name]
        xm = m['model'].domain.convert(x)[0].reshape(1, -1)
        # print(f'xm = {xm}')
        y_calc = m['model'].predict(xm)         # ([1], [[1, 2]])
        y_proba = m['model'].predict_proba(xm)  # [[1, 2]]

        y.update({
            name: [y_calc, y_proba]
        })
        metrics.update({
            name: m['passport']['metrics']
        })
        # print(f'{m} (y_calc) = {y_calc}, y_proba) = {y_proba}')
        # метрики из экземпляра модели (если есть)
        # ex:
        # mb = m['model']
        # p = mb._score.CA
        save_model_passport(m)

    # print(f'y = {y} \n metrics = {metrics}')
    print('\n--> Calculated successful!')
    return y, metrics


def save_model_passport(model):
    slash = '\\'
    m = model['model']
    mpass = model['passport']

    mpass['model_type'] = str(type(m))
    mpass['input_features_names'] = [str(v) for v in m.domain.attributes]
    mpass['output_features_names'] = [str(v) for v in m.domain.class_vars]

    pass_path = slash.join(mpass['train_dataset_filename'].split(slash)[:-1]) + slash
    filename = mpass['id'] + '.json'
    file_path = pass_path + filename

    with open(file_path, 'w') as file:
        json.dump(mpass, file)
        print(f'--> Passport model file "{filename}" is saved!')


def save_model(model, file_path):
    # сохранить модель
    with open(file_path, mode='wb') as file:
        pk.dump(model, file)
        print('--> Binary model file is saved!')
