from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
import json,os

f = open('AverageOfFirst.json', encoding='utf-8')
res = f.read()
data = json.loads(res)
data.insert(0,0)

f = open('AverageOfSecond.json', encoding='utf-8')
res = f.read()
data2 = json.loads(res)
data2.insert(0,0)
data2.insert(0,data[0])

mPath = "..\\codeSimFileAll\\49405"
id_list=os.listdir(mPath)



simOf1 = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
        .add_xaxis(id_list)
        .add_yaxis("第一题", data)
        .add_yaxis("第二题",data2)
        .set_global_opts(
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-90)),
        title_opts=opts.TitleOpts(title="第1、2题相似度分布"),
        datazoom_opts=opts.DataZoomOpts(),
    )
        .render("simTotal.html")
)

list2 = [
    {"value": 192, "percent": 192 / 199}

]

list3 = [
    {"value": 7, "percent": 7 / 199}

]

c = (
    Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
    .add_xaxis([1])
    .add_yaxis("Over30%", list2, stack="stack1", category_gap="50%")
    .add_yaxis("Under30%", list3, stack="stack1", category_gap="50%")
    .set_series_opts(
        label_opts=opts.LabelOpts(
            position="right",
            formatter=JsCode(
                "function(x){return Number(x.data.percent * 100).toFixed() + '%';}"
            ),
        )
    )
    .render("stack_bar_percent.html")
)

