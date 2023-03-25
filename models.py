# словарь моделей
models = {
    'Tree': {
        'model': None,  # бинарный экземпляр модели
        'passport': {
            'id': 'tree(bin-2-5-3)v1',  # параметры в окне модели сверху вниз
            'name': 'Квалификация фирмы как мошенника по данным аудита',
            'model_type': '',
            'requires_normalized_data': False,
            'requires_standardized_data': False,
            'input_features_names': [],
            'output_features_names': [],
            'metrics': {
                'CA': 0.961
            },
            'train_dataset_filename': 'Z:\\Documents\\LEARNING\\Магистратура НГТУ\\ИАДиМО\\2023\\data_sets\\audit_data\\audit_risk_clean.csv',
            'model_filename': 'Z:\\Documents\\LEARNING\\Магистратура НГТУ\\ИАДиМО\\2023\\models\\clf_tree.pkcls',
        },
    },
    'Random Forest': {
        'model': None,
        'passport': {
            'id': 'rforest(5-3-5)v1',
            'name': 'Квалификация фирмы как мошенника по данным аудита',
            'model_type': '',
            'requires_normalized_data': False,
            'requires_standardized_data': False,
            'input_features_names': [],
            'output_features_names': [],
            'metrics': {
                'CA': 0.97
            },
            'train_dataset_filename': 'Z:\\Documents\\LEARNING\\Магистратура НГТУ\\ИАДиМО\\2023\\data_sets\\audit_data\\audit_risk_clean.csv',
            'model_filename': 'Z:\\Documents\\LEARNING\\Магистратура НГТУ\\ИАДиМО\\2023\\models\\clf_rforest.pkcls',
        },
    },
    'Neuro Net': {
        'model': None,
        'passport': {
            'id': 'nn(100-relu-adam)v1',
            'name': 'Квалификация фирмы как мошенника по данным аудита',
            'model_type': '',
            'requires_normalized_data': False,
            'requires_standardized_data': False,
            'input_features_names': [],
            'output_features_names': [],
            'metrics': {
                'CA': 0.905
            },
            'train_dataset_filename': 'Z:\\Documents\\LEARNING\\Магистратура НГТУ\\ИАДиМО\\2023\\data_sets\\audit_data\\audit_risk_clean.csv',
            'model_filename': 'Z:\\Documents\\LEARNING\\Магистратура НГТУ\\ИАДиМО\\2023\\models\\clf_nnet.pkcls',
        },
    },
    'Logistic Regression': {
        'model': None,
        'passport': {
            'id': 'logregr(L2-C1)v1',
            'name': 'Квалификация фирмы как мошенника по данным аудита',
            'model_type': '',
            'requires_normalized_data': False,
            'requires_standardized_data': False,
            'input_features_names': [],
            'output_features_names': [],
            'metrics': {
                'CA': 0.948
            },
            'train_dataset_filename': 'Z:\\Documents\\LEARNING\\Магистратура НГТУ\\ИАДиМО\\2023\\data_sets\\audit_data\\audit_risk_clean.csv',
            'model_filename': 'Z:\\Documents\\LEARNING\\Магистратура НГТУ\\ИАДиМО\\2023\\models\\clf_logregr.pkcls',
        },
    },
}