from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.validators import Auto
from reportlab.graphics.charts.legends import Legend
from reportlab.graphics.charts.piecharts import Pie
from reportlab.graphics.shapes import Drawing, String
from reportlab.platypus import SimpleDocTemplate, Paragraph

def Fruits():
    fruits = {
        "Elderberries":1,
        "Figs":1,
        "Apples":2,
        "Durians":3,
        "Bananas":5,
        "Cheries":8,
        "Grapes":13,
        "Strawberry":20
    }
    return fruits


def add_legend(draw_obj, chart, data):
    legend = Legend()
    legend.alignment = 'right'
    legend.x = 10
    legend.y = 70
    legend.colorNamePairs = Auto(obj=chart)  # type: ignore    draw_obj.add(legend)
    
def pie_chart_with_legend():
    drawing = Drawing(width=400, height=200)
    my_title = String(170, 40, 'My Pie Chart', fontSize=14)
    pie = Pie()
    pie.sideLabels = True
    pie.x = 150
    pie.y = 65
    fruits = Fruits()
    label_items=[]
    data =[]
    for fruit in fruits:
        data.append(fruits[fruit])
        label_items.append(fruit)
    pie.labels = label_items  # type: ignore   
    pie.data = data
    pie.slices.strokeWidth = 0.5
    drawing.add(my_title)
    drawing.add(pie)
    add_legend(drawing, pie, data)
    return drawing
def main():
    doc = SimpleDocTemplate('test.pdf')
    
    elements = []
    styles = getSampleStyleSheet()
    ptext = Paragraph('Text before the chart', styles["Normal"])
    elements.append(ptext)
    
    chart = pie_chart_with_legend()
    elements.append(chart)
    
    ptext = Paragraph('Text after the chart', styles["Normal"])
    elements.append(ptext)
    doc.build(elements)
    
if __name__ == '__main__':
    main()