# Data_Set given below
# Note this course is taken with Non-English, so given data is Non-English too

# Pie chart data_A
data_A = [("天河区",164),("越秀区",69),("海珠区",68),("荔湾区",27),("番禺区",23),("白云区",20),("黄埔区",1)]
# Bar chart x1,y1
x1 = ["珠江新城","天河城/体育中心","北京路","江南西","天河北","机场路",
         "江南大道","高德置地/花城汇","石牌/龙口","兴盛路/跑马场"]
y1 = [60, 42, 34, 23, 22, 10, 10, 10, 10, 10]
# Rose data_B
data_B = [("四星商户",175),("准五星商户",156),("五星商户",34),("准四星商户",7)]
# Bar chart x2,y2
x2 = ["江浙菜", "茶餐馆", "小龙虾", "海鲜", "素菜", "湘菜", "韩式料理", "创意菜", "韩国料理", "茶餐厅", "川菜",
        "东南亚菜", "咖啡厅", "烧烤", "自助餐", "面包甜点", "火锅", "日本料理", "粤菜", "西餐"]
y2 = [3, 3, 4, 4, 5, 6, 6, 7, 9, 9, 11, 11, 14, 18, 20, 21, 43, 52, 53, 61]
# Heat chart x and y
heat_x = ["评论数","人均价格","口味评分","环境评分","服务评分"]
heat_y = ["评论数","人均价格","口味评分","环境评分","服务评分"]
# Heat chart value
value = [[0,0,1.00],[0,1,0.04],[0,2,-0.07],[0,3,-0.05],[0,4,-0.28],
         [1,0,0.04],[1,1,1.00],[1,2,0.13],[1,3,0.40],[1,4,0.33],
         [2,0,-0.07],[2,1,0.13],[2,2,1.00],[2,3,0.25],[2,4,0.52],
         [3,0,-0.05],[3,1,0.40],[3,2,0.25],[3,3,1.00],[3,4,0.68],
         [4,0,-0.28],[4,1,0.33],[4,2,0.52],[4,3,0.68],[4,4,1.00]]
# Map data: data_C
data_C = [("天河区",164),("越秀区",69),("海珠区",68),("荔湾区",27),("番禺区",23),("白云区",20),("黄埔区",1)]
# Radar data
sx = [[4.1,4.2,3.7,4.5,4.2]]
zwx = [[4.5,4.7,4.2,4.5,4.8]]
wx = [[4.6,4.9,4.9,5,4.3]]
zsx = [[4.3,3.7,4.1,4.1,4.6]]
# schema
c_schema = [
    {"name": "菜价菜量", "max": 5},
    {"name": "口味", "max": 5},
    {"name": "环境", "max": 5},
    {"name": "服务", "max": 5},
    {"name": "交通", "max": 5}]
# Relation category
category = [{"name":"四星推荐"}, {"name":"准五星推荐"}, {"name":"五星推荐"}, {"name":"准四星推荐"}]
# 关系图数据nodes_list,links_list
nodes_list = [{"id":"四星商户", "name":"四星商户", "category":0, "symbolSize":30},
              {"id":"准五星商户", "name":"准五星商户", "category":1, "symbolSize":30},
              {"id":"五星商户", "name":"五星商户", "category":2, "symbolSize":30},
              {"id":"准四星商户", "name":"准四星商户", "category":3, "symbolSize":30},
              {"id":"Mr Pilot飞行先生", "name":"Mr Pilot飞行先生", "category":0, "symbolSize":10},
              {"id":"香草烤土豆", "name":"香草烤土豆", "category":0, "symbolSize":10},
              {"id":"香伯爵自助餐厅", "name":"香伯爵自助餐厅", "category":0, "symbolSize":10},
              {"id":"三文鱼刺身", "name":"三文鱼刺身", "category":0, "symbolSize":10},
              {"id":"佬麻雀", "name":"佬麻雀", "category":0, "symbolSize":10},
              {"id":"金沙红米肠", "name":"金沙红米肠", "category":0, "symbolSize":10},
              {"id":"高卡一番日本料理", "name":"高卡一番日本料理", "category":1, "symbolSize":10},
              {"id":"芝士牛舌", "name":"芝士牛舌", "category":1, "symbolSize":10},
              {"id":"Cocina科奇娜·南美创意料理", "name":"Cocina科奇娜·南美创意料理", "category":1, "symbolSize":10},
              {"id":"牛肉寿司", "name":"牛肉寿司", "category":1, "symbolSize":10},
              {"id":"Ebony", "name":"Ebony", "category":1, "symbolSize":10},
              {"id":"烟三文鱼沙拉", "name":"烟三文鱼沙拉", "category":1, "symbolSize":10},
              {"id":"神隐酒场", "name":"神隐酒场", "category":2, "symbolSize":10},
              {"id":"玫瑰露酒煮海螺", "name":"玫瑰露酒煮海螺", "category":2, "symbolSize":10},
              {"id":"渔意如意", "name":"渔意如意", "category":2, "symbolSize":10},
              {"id":"一鱼五食", "name":"一鱼五食", "category":2, "symbolSize":10},
              {"id":"四海一家", "name":"四海一家", "category":2, "symbolSize":10},
              {"id":"碳烧生蚝", "name":"碳烧生蚝", "category":2, "symbolSize":10},
              {"id":"RIBS乐排馆", "name":"RIBS乐排馆", "category":3, "symbolSize":10},
              {"id":"和牛牛腩", "name":"和牛牛腩", "category":3, "symbolSize":10},
              {"id":"98农庄", "name":"98农庄", "category":3, "symbolSize":10},
              {"id":"炭烧牛蛙紫苏味平锅", "name":"炭烧牛蛙紫苏味平锅", "category":3, "symbolSize":10},
              {"id":"悦榕庄", "name":"悦榕庄", "category":3, "symbolSize":10},
              {"id":"佛跳墙", "name":"佛跳墙", "category":3, "symbolSize":10}]

links_list =  [{"source":"四星商户", "target":"Mr Pilot飞行先生"},
               {"source":"四星商户", "target":"香伯爵自助餐厅"},
               {"source":"四星商户", "target":"佬麻雀"},
               {"source":"准五星商户", "target":"高卡一番日本料理"},
               {"source":"准五星商户", "target":"Cocina科奇娜·南美创意料理"},
               {"source":"准五星商户", "target":"Ebony"},
               {"source":"五星商户", "target":"神隐酒场"},
               {"source":"五星商户", "target":"渔意如意"},
               {"source":"五星商户", "target":"四海一家"},
               {"source":"准四星商户", "target":"RIBS乐排馆"},
               {"source":"准四星商户", "target":"98农庄"},
               {"source":"准四星商户", "target":"悦榕庄"},
               {"source":"Mr Pilot飞行先生", "target":"香草烤土豆"},
               {"source":"香伯爵自助餐厅", "target":"三文鱼刺身"},
               {"source":"佬麻雀", "target":"金沙红米肠"},
               {"source":"高卡一番日本料理", "target":"芝士牛舌"},
               {"source":"Cocina科奇娜·南美创意料理", "target":"牛肉寿司"},
               {"source":"Ebony", "target":"烟三文鱼沙拉"},
               {"source":"神隐酒场", "target":"玫瑰露酒煮海螺"},
               {"source":"渔意如意", "target":"一鱼五食"},
               {"source":"四海一家", "target":"碳烧生蚝"},
               {"source":"RIBS乐排馆", "target":"和牛牛腩"},
               {"source":"98农庄", "target":"炭烧牛蛙紫苏味平锅"},
               {"source":"悦榕庄", "target":"佛跳墙"}]






# Projects start here
from pyecharts.charts import Pie,Bar,HeatMap,Map,Radar,Graph,Page

from pyecharts import options as opts

def pie():

    c = Pie(init_opts=opts.InitOpts(theme="purple-passion"))

    c.add("", 
        data_pair=data_A,
        label_opts=opts.LabelOpts(formatter="{b}: {c}")
        )
    c.set_global_opts(title_opts=opts.TitleOpts(title="行政区美食占比"))
    return c

def bar(): 
    c = Bar(init_opts=opts.InitOpts(theme="purple-passion"))
    c.add_xaxis(x1)
    c.add_yaxis("",y1)
    c.set_global_opts(
            title_opts=opts.TitleOpts(title="商圈分布"),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)))
    return c

def pie_circle():

    c = Pie(init_opts=opts.InitOpts(theme="purple-passion"))
    c.add(
        "",
        data_pair=data_B,
        radius=["40%", "55%"],
        rosetype="area"
    )
    c.set_global_opts(title_opts=opts.TitleOpts(title="星级占比"))
    return c
def bar_reverse():

    c = Bar(init_opts=opts.InitOpts(theme="purple-passion"))

    c.add_xaxis(x2)
    c.add_yaxis("", y2)
    c.reversal_axis()
    c.set_series_opts(label_opts=opts.LabelOpts(position="right"))

    c.set_global_opts(title_opts=opts.TitleOpts(title="美食种类分布"))
    return c

def heat_corr():

    c = HeatMap(init_opts=opts.InitOpts(theme="purple-passion"))
    c.add_xaxis(heat_x)

    c.add_yaxis(
            "",
            heat_y,
            value,
            label_opts=opts.LabelOpts(position="inside")
        )
    c.set_global_opts(
        title_opts=opts.TitleOpts(title="价格口碑等相关性"),
        visualmap_opts=opts.VisualMapOpts(is_show=False,min_=-1,max_=1)
        )

    return c

def map_chart():
    
    c = Map(init_opts=opts.InitOpts(theme="purple-passion"))

    c.add(
        "", 
        data_pair=data_C, 
        maptype="广州"
        )

    c.set_global_opts(
        title_opts=opts.TitleOpts(title="广州美食分布"),
        visualmap_opts=opts.VisualMapOpts()
        )
   # return返回c
    return c

def radar():

    c = Radar(init_opts=opts.InitOpts(theme="purple-passion"))

    c.add_schema(schema=c_schema)

    c.add("四星商户",
        sx,
        color = "#6495ed",
        areastyle_opts = opts.AreaStyleOpts(opacity = 0.1),
        label_opts=opts.LabelOpts(is_show=False))
    c.add("准五星商户",
        zwx,
        color = "#696969",
        areastyle_opts = opts.AreaStyleOpts(opacity = 0.1),
        label_opts=opts.LabelOpts(is_show=False))

    c.add("五星商户",
        wx,
        color = "#3cb371",
        areastyle_opts = opts.AreaStyleOpts(opacity = 0.1),
        label_opts=opts.LabelOpts(is_show=False))

    c.add("准四星商户",
        zsx,
        color = "#ff8c00",
        areastyle_opts = opts.AreaStyleOpts(opacity = 0.1),
        label_opts=opts.LabelOpts(is_show=False))
    c.set_global_opts(title_opts=opts.TitleOpts(title="星级商铺评分"))

    return c

def graph_chart():

    c.add(
        "",
        categories=category,
        nodes=nodes_list,
        links=links_list,
        layout="circular",
        is_rotate_label=True,
        linestyle_opts=opts.LineStyleOpts(color="source", curve=0.3)
            )
    c.set_global_opts(
        legend_opts=opts.LegendOpts(orient="vertical", pos_left="3%", pos_top="20%"),
        title_opts=opts.TitleOpts(title="星级推荐")
    )
    return c

page = Page(layout=Page.DraggablePageLayout)

page.add(
    pie(),
    bar(),
    pie_circle(),
    bar_reverse(),
    heat_corr(),
    map_chart(),
    radar(),
    graph_chart()
)

page.render("/Users/mumu/pagetest.html")

Page.save_resize_html("/Users/mumu/page.html", cfg_file="/Users/mumu/page.json",dest="/Users/mumu/GuangZhou.html")

