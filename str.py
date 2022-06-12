import streamlit as st
import pandas as pd
import streamlit.components.v1 as components

def nav1():
    df=pd.read_csv("US Superstore data.csv")
    st.dataframe(df,height=500,width=800)

selected=st.sidebar.radio("Main Menu",['About','View Data','Visualize','Time Series Analysis','Future Sales Prediction'])    

if selected =='About':
    st.title("About")
    st.write("Abstract")
    
elif selected=='View Data':
    st.title("Data")
    nav1()
        
    
elif selected=='Visualize':
    st.title("Visualizations using tableau")
    html_temp = "<div class='tableauPlaceholder' id='viz1655040790932' style='position: relative'><noscript><a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SuperstoreSalesAnalysis_16550189883770&#47;DB3&#47;1_rss.png' style='border: none' /></a></noscript><object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='SuperstoreSalesAnalysis_16550189883770&#47;DB3' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Su&#47;SuperstoreSalesAnalysis_16550189883770&#47;DB3&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' /></object></div>                <script type='text/javascript'>                    var divElement = document.getElementById('viz1655040790932');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='100%';vizElement.style.height=(divElement.offsetWidth*0.75)+'px';} else { vizElement.style.width='100%';vizElement.style.minHeight='1700px';vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>"
    components.html(html_temp, height=800, width=900, scrolling=True)
            
    
elif selected=='Time Series Analysis':
    rmse=[]
    with open("rmse.txt","r") as f:
        for i in f.readlines():
            rmse.append(round(eval(i),3))
    
    st.title('Time Series Analysis of the Superstore sales')
    st.write("\nGiven data (non -stationary time series data)")
    st.image("databefore.png")
            
    st.write("\n\n")
    st.write("After making data stationary:")
    st.image("dataafter.png")
    
    st.write("\n\n")
    st.subheader("Auto-correlation (ACF) and Partial Auto-correlation (PACF) functions")
    st.image("ACF_PACF.png")
    
    st.header("Time Series Models")
    
    st.subheader("Autoregressive Model AR(3)")
    st.image("AR(3).png")
    st.write("RMSE : "+str(rmse[0]))
    
    st.subheader("Moving Average Model MA(2)")
    st.image("MA(2).png")
    st.write("RMSE : "+str(rmse[1]))
    
    st.subheader("ARIMA Model")
    st.image("ARIMA.png")
    st.write("RMSE : "+str(rmse[2]))
    
    st.subheader("SARIMAX Model")
    st.image("SARIMAX.png")
    st.write("RMSE : "+str(rmse[3]))
    
    st.write("\n\nWe can observe the minimum RMSE is obtained when the data is fit into a SARIMAX model. Hence we use the same to predict future sales(until 2021).")
    
    
else:
    st.title('Future Sales Prediction')
    st.write("The dataset contains the sales records for four years (2014-2017). Using the time series model built, future sales has been predicted until 2021.")
    st.image("future.png")
    
