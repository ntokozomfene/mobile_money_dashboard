#installing modules 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import dash
import dash_core_components as dcc
import dash_html_components as html
import numpy as np
import plotly.offline as pyo
import plotly.graph_objects as go
import plotly.express as px
training = pd.read_csv('training.csv')

# renaming columns
training.rename(columns={'Q1':'age','Q2':'gender','Q3':'marital_status','Q4':'highest education','Q5':'Which_of_the_following_applies_to_you?','Q6':'land_owner','Q7':'own_a_mobile','Q8_1':'salaries','Q8_2':'money_from_trading','Q8_3':'money_from_providing_service','Q8_4':'piece_work','Q8_5':'rental_income','Q8_6':'interest_from_savings','Q8_7':'Pension','Q8_8':'social_welfare_money','Q8_9':'rely_on_someone_else','Q8_10':"don't_get_money",'Q8_11':'other','Q11':'providing_service', 'Q10':'types_of_income'}, inplace=True)
number_to_gender= {1:'female',2:'male'
}
mobile_mney={0:'no',1:'yes'  
}
mmc= {0:'no_mobile_money',1:'one_finacial_service',2:'mobile_money_only',3:'mobile_money_and_other'
}
ms={1:'married',2:'divorced',3:'widowed',4:'single/never_married'
}
svng={0:'no',1:'yes'
}
lo={1:'yes',2:'no'
}
qy={-1:'not_applicable',1:'never',2:'daily',3:'weekly',4:'monthly',5:'less_often'
}

typ={
    -1:'Not applicable',1:'Personalservices',
    2:'Telecommunications/IT',3:'Financialservices',
    4:'Transport',5:'Hospitality',
    6:'Information/Research',7:'Technical',
    8:'Childcare',9:'Healthservices',
    10:'Legalservices',11:'Security',
    12:'Other'   
}
types={
    -1:'Not applicable',
    1:'Produce I grow',
    2:'Products from livestock',
    3:'Livestock',
    4:'Aquaculture',
    5:'Agricultural products',
    6:'Non-agricultural products',
    7:'Things you make',
    8:'Collection from nature',
    9:'Things you process',
    10:'Other'
}
training.providing_service = training.providing_service.map(typ)
training.types_of_income = training.types_of_income.map(types)
training.gender = training.gender.map(number_to_gender)
training.mobile_money_classification = training.mobile_money_classification.map(mmc)
training.marital_status = training.marital_status.map(ms)
training.mobile_money = training.mobile_money.map(mobile_mney)
training.savings = training.savings.map(svng)
training.land_owner = training.land_owner.map(lo)
training.Q16 = training.Q16.map(qy)
training.Q17 = training.Q17.map(qy)
male = training[training.gender=='male']
female = training[training.gender=='female']


m_money = training[training.mobile_money=='yes']
marital_q16 = m_money.groupby(['marital_status', 'Q16'])['marital_status'].count().unstack('Q16').fillna(0)

divorced = [5,120,37,207,14]
married = [47,727,350,1278,148]
single = [22,203,120,323,71]
widowed = [2,74,30,139,13]
animals=['daily', 'less_often', 'monthly','never','weekly']

app = dash.Dash()


app.layout = html.Div([
            html.H1('Mobile money Dashboard',style={'textAlign':'center',
                                          'color':'#111111','paper_bgcolor':'#726F6E'}),
                        html.Div([dcc.Graph(id='Mobile_money_BAR_GRAPH',
                      figure={'data':[go.Bar(x=training.mobile_money_classification.values,y=training.index)
                                                                   ],
                            'layout':go.Layout(title='mobile money classification graph',plot_bgcolor='#726F6E',paper_bgcolor='#8B5245',font_color='#FCFBF0')})
                                  ],style={'color':'red','border':'2px red solid'})
            ,


        
                        html.Div([dcc.Graph(id='male',
                      figure={'data':[go.Pie(labels=['mobile_money_and_other','no_mobile_money','one_finacial_service','mobile_money_only'],
                                            values=np.array(male.mobile_money_classification.value_counts())),
                                    ],

                              'layout':go.Layout(title='male pie chart',plot_bgcolor='#726F6E',paper_bgcolor='#8B5245',font_color='#FCFBF0')})
            ,
    
                        dcc.Graph(id='Female',
                      figure={'data':[go.Pie(labels=['mobile_money_and_other','no_mobile_money','one_finacial_service','mobile_money_only'],
                                            values=np.array(female.mobile_money_classification.value_counts())),
                                    ],

                              'layout':go.Layout(title='Female pie chart',plot_bgcolor='#726F6E',paper_bgcolor='#8B5245',font_color='#FCFBF0')})
                                  ],style={'color':'red','border':'2px red solid'})
    
            ,
                        html.Div([dcc.Graph(id='BAR_GRAPH',
                      figure={'data':[go.Bar(x=training.age,y=training.mobile_money)
                                      
                             ],
                            'layout':go.Layout(title='BAR GRAPH AGE',plot_bgcolor='#726F6E',paper_bgcolor='#8B5245',font_color='#FCFBF0')})
                                  ],style={'color':'red','border':'2px red solid'})

            ,
                        html.Div([dcc.Graph(id='marital stacked bargraph',
                      figure={'data':[
                          go.Bar(name='Divorced', x=animals, y=divorced),
                          go.Bar(name='Single', x=animals, y=single),
                          go.Bar(name='Married', x=animals, y=married),
                          go.Bar(name='Widowed', x=animals, y=widowed)
                      ],
                      'layout':go.Layout(title='marital stacked bargraph',barmode='stack',plot_bgcolor='#726F6E',paper_bgcolor='#8B5245',font_color='#FCFBF0')})
                                  
                                 ],style={'color':'red','border':'2px red solid'})
                                
])
                     




if __name__ =='__main__':
    app.run_server()