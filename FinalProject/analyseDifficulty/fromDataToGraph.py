import json
from pyecharts import options as opts
from pyecharts.charts import Bar, Line
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import pandas as pd


def getMax(l):
    max = 0
    min = 1000
    for i in l:
        if i['value'] > max:
            max = i['value']
        elif i['value'] < min:
            min = i['value']
    return max - min


f1 = open('length.json', encoding='utf-8')  #
res1 = f1.read()
len_list = json.loads(res1)
f2 = open('id.json', encoding='utf-8')  #
res2 = f2.read()
id_list = json.loads(res2)
f3 = open('score.json', encoding='utf-8')  #
res3 = f3.read()
score_list = json.loads(res3)
f4 = open('time.json', encoding='utf-8')  #
res4 = f4.read()
time_list = json.loads(res4)
f5 = open('length_all.json', encoding='utf-8')  #
res5 = f5.read()
len_all = json.loads(res5)
f6 = open('score_all.json', encoding='utf-8')  #
res6 = f6.read()
score_all = json.loads(res6)
f7 = open('time_all.json', encoding='utf-8')  #
res7 = f7.read()
time_all = json.loads(res7)
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()
f6.close()
f7.close()

for i in range(len(id_list)):
    len_series = pd.Series(len_all[i])
    score_series = pd.Series(score_all[i])
    time_series = pd.Series(time_all[i])
    len_list[i] = {"value": len_list[i], "skew": len_series.skew(), "kurt": len_series.kurt()}
    score_list[i] = {"value": score_list[i], "skew": score_series.skew(), "kurt": score_series.kurt()}
    time_list[i] = {"value": time_list[i], "skew": time_series.skew(), "kurt": time_series.kurt()}

length = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(id_list)
        .add_yaxis("相同caseId代码平均代码长度", len_list)
        .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter=JsCode(
                "function(x){return 偏度：x.data.skew+峰度:+x.data.kurt;}"
            ),
        )
    )
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-90)),
        title_opts=opts.TitleOpts(title="代码长度分布"),
        datazoom_opts=opts.DataZoomOpts(),
    )
        .render("code_len.html")
)

score = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(id_list)
        .add_yaxis("相同caseId代码平均的平均每次成绩", score_list)
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-90)),
        title_opts=opts.TitleOpts(title="代码平均每次成绩"),
        datazoom_opts=opts.DataZoomOpts(),
    )
        .render("code_score.html")
)

time = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(id_list)
        .add_yaxis("相同caseId代码平均运行时间", time_list)
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-90)),
        title_opts=opts.TitleOpts(title="代码平均运行时间分布"),
        datazoom_opts=opts.DataZoomOpts(),
    )
        .render("code_times.html")
)
# TODO  做一个长度和运行时间的双重Y轴图 研究它们之间互相影响
len_time = (
    Bar(init_opts=opts.InitOpts(width="1600px", height="800px"))
        .add_xaxis(xaxis_data=id_list)
        .add_yaxis(
        series_name="代码长度",
        y_axis=len_list,
        label_opts=opts.LabelOpts(is_show=False),
    )
        .extend_axis(
        yaxis=opts.AxisOpts(
            name="代码运行时间",
            type_="value",
            # min_=0,
            # max_=25,
            # # interval=5,
            axislabel_opts=opts.LabelOpts(formatter="{value} s"),
        )
    )
        .set_global_opts(
        tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="cross"
        ),
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),
        yaxis_opts=opts.AxisOpts(
            name="代码运行时间",
            type_="value",
            # min_=0,
            # max_=250,
            # interval=50,
            axislabel_opts=opts.LabelOpts(formatter="{value} s"),
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        datazoom_opts=opts.DataZoomOpts(),
    )
)

line = (
    Line()
        .add_xaxis(xaxis_data=id_list)
        .add_yaxis(
        series_name="代码运行时间",
        yaxis_index=1,
        y_axis=time_list,
        label_opts=opts.LabelOpts(is_show=False),
    )
)

len_time.overlap(line).render("len_time.html")

res = []
span_len = getMax(len_list)
span_score = getMax(score_list)
span_time = getMax(time_list)
for i in range(len(id_list)):
    temp = 100 * (0.5 * len_list[i]['value'] / span_len + 0.2 * time_list[i]['value'] / span_time + 0.3 * score_list[i][
        'value'] / span_score)
    res.append(temp)

result = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(id_list)
        .add_yaxis("代码难度（满分100）", res)
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-90)),
        title_opts=opts.TitleOpts(title="代码难度"),
        datazoom_opts=opts.DataZoomOpts(),
    )
        .render("code_difficulty.html")
)
