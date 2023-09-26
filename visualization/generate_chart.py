


import pandas as pd
import plotly.express as px
import json

def generate_chart(file,columns,chosenReq,chart,selectedCustom):
    try:

        x_axis = columns.get("X Axis", None)
        y_axis = columns.get("Y Axis", None)
        hue_column = columns.get("hue", None)
        chart_function = getattr(px, chart)

        if x_axis is not None:
            kwargs = {"x": x_axis}
            if y_axis is not None:
                kwargs["y"] = y_axis
            if hue_column is not None:
                kwargs["color"] = hue_column
        elif y_axis is not None:
            kwargs = {"y": y_axis}
            if hue_column is not None:
                kwargs["color"] = hue_column

   
        df = pd.read_csv(file)
        fig = chart_function(df, **kwargs)

        if chart in ["line", "area", "scatter"]:
           fig.update_traces(
            line_shape=selectedCustom.get("Line Shape"),
            line_dash=selectedCustom.get("Line Dash")
        ) 
           
        Template = selectedCustom.get("Template")
        title = selectedCustom.get("title")
        title_color = selectedCustom.get("Title Color")
        fig.update_layout(template=Template,
            title={
            "text": title,
            "font": {"color": title_color}
            }
        )

        return fig
    except Exception as e:
        print(e)
        return {'error': str(e)}


