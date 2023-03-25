import streamlit as st, pandas as pd
from mlearn import models_calc, models

# режим сбора данных
mode = {
	'test': 0,		# из тестового набора
	'inputs': 1		# из полей ввода Х
}

# тестовые наборы
test_data = {
	# [x0, x1, x2, y]
	'test 1': [1.548, 2.0, 0.74, 0],
	'test 2': [9.384, 3.0, 10.96, 1],
	'test 3': [1.604, 2.0, 1.02, 0],
}
test_options = [key for key in test_data.keys()]
start_index = 0
dataset = list(test_data.keys())[start_index]

# globals
y = metrics = 0
y_none = '?'
columns = ['Inherent_Risk', 'Score', 'TOTAL', 'Risk (fact)'] 	# 'Risk (calculated)']


def get_test_data(tst):
	# выбор тестового набора
	global test_data, columns
	frm = pd.DataFrame([test_data[tst]], index=['x0 ... x2 | Y'], columns=columns)
	return frm


def processing(mod):
	# подготовка и отправка данных на расчет
	global test, y, metrics
	if mod:
		# сборка данных полей ввода
		data = pd.DataFrame([[inherent_risk, score, total, None]], index=['x0 ... x2 | Y'], columns=columns)
		x = data.iloc[0, :4]
		name = 'значения Х'
	else:
		# данные тестового набора
		data = get_test_data(test)
		x = data.iloc[0, :4]
		name = test
	data_info(data, name)
	# вычисление и отправка данных на визуализацию
	y, metrics = models_calc(x)
	render_result(y, metrics)


def data_info(dset, name):
	# вывод таблицы данных
	cnt.info(f'Набор данных: *{name}*')
	cnt.table(dset)


def render_result(res, scores):
	global cols
	# отрисовка результатов вычисления
	if res:
		# колонки в контейнере
		with cnt:
			for i in range(len(model_names)):
				with cols[i]:
					print(f'Метрики:  {scores}')
					name = model_names[i]
					st.info(f'{name}\n')
					if name in res:
						# вывод значений модели
						val = 'Да' if res[name][0][0] > 0 else 'Нет'
						# y = pd.DataFrame(val, columns=['Risk'], index=[''])
						val1 = res[name][1][0].max()
						yp = pd.DataFrame([[val, val1]], columns=['Risk', 'Вероятность'], index=[''])
						# st.write(y)
						st.table(yp)
						# метрики модели
						ac = pd.DataFrame([scores[name].values()], columns=['Точность'],
										  index=[k for k in scores[name].keys()])
						st.table(ac)


# ОСНОВНОЙ БЛОК СТРАНИЦЫ
cnt = st.container()
# заголовок страницы
cnt.title('Оценка моделей классификации')

# колонки моделей
model_names = [name for name in models.keys() if 'Tree' not in name]  # оставляем 3 модели
cols = list(st.columns(len(model_names), gap='large'))

# БОКОВАЯ ПАНЕЛЬ
st.sidebar.header('Входные данные:')

# выбор тестов
test = st.sidebar.selectbox('*Тестовые наборы:*', test_options, index=start_index,
							on_change=processing, args=[mode['test']],
							kwargs=None, disabled=False, label_visibility='visible')

st.sidebar.write('---')
st.sidebar.write('*Значения Х:*')

# поля ввода значений x
inherent_risk = st.sidebar.number_input('Inherent_Risk:', min_value=0.1, max_value=1000., value=500., step=0.1,
										format=None, on_change=None, args=None, kwargs=None,
										disabled=False, label_visibility='visible')

score = st.sidebar.slider('Score:', min_value=0.1, max_value=10., value=6., step=0.02, format=None,
						  on_change=None, args=None, kwargs=None, disabled=False, label_visibility='visible')

total = st.sidebar.number_input('TOTAL:', min_value=0., max_value=1500., value=500., step=0.1, format=None,
								on_change=None, args=None, kwargs=None, disabled=False, label_visibility='visible')

st.sidebar.write('')

# кнопка запуска расчета
st.sidebar.button('Рассчитать риск', key=None, help='', on_click=processing, args=[mode['inputs']], kwargs=None,
				  type="secondary", disabled=False, use_container_width=False)
