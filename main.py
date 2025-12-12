import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

# Combine and process sales data
combined_data = []

for i in range(0, 3):
    file_path = f"data/daily_sales_data_{i}.csv"
    read = pd.read_csv(file_path)

    # Filter rows and create a copy to avoid SettingWithCopyWarning
    filter_data = read.loc[read['product'] == 'pink morsel'].copy()

    # Calculate sales
    filter_data['sales'] = filter_data['price'].str.replace('$', '').astype(float) * filter_data['quantity']

    # Select relevant columns
    processed_data = filter_data[['sales', 'date', 'region']]

    # Append to the list
    combined_data.append(processed_data)

# Combine all DataFrames into one
overall_data = pd.concat(combined_data)

# Save to a new CSV file
overall_data.to_csv("data/combined_sales_data.csv", index=False)

# Dash app for visualizing sales data
app = Dash()

# Load the combined data produced earlier
df = pd.read_csv("data/combined_sales_data.csv")

# Dash layout with styling
app.layout = html.Div([
    html.Div([
        html.H1('Soul Foods — Pink Morsel Sales Visualiser', 
                style={
                    'textAlign': 'center',
                    'color': '#2c3e50',
                    'marginBottom': '30px',
                    'fontFamily': 'Arial, sans-serif'
                }),
        
        html.Div([
            html.Label('Select Region:', 
                      style={
                          'fontWeight': 'bold',
                          'marginBottom': '10px',
                          'color': '#34495e',
                          'fontFamily': 'Arial, sans-serif'
                      }),
            dcc.RadioItems(
                id='region-filter',
                options=[
                    {'label': html.Span('All Regions', style={'color': '#2c3e50', 'fontWeight': 'bold'}), 'value': 'all'},
                    {'label': html.Span('North', style={'color': '#e74c3c', 'fontWeight': 'bold'}), 'value': 'north'},
                    {'label': html.Span('East', style={'color': '#3498db', 'fontWeight': 'bold'}), 'value': 'east'},
                    {'label': html.Span('South', style={'color': '#f39c12', 'fontWeight': 'bold'}), 'value': 'south'},
                    {'label': html.Span('West', style={'color': '#27ae60', 'fontWeight': 'bold'}), 'value': 'west'}
                ],
                value='all',
                style={
                    'marginBottom': '20px',
                    'fontFamily': 'Arial, sans-serif'
                },
                inputStyle={'margin': '5px'},
                labelStyle={'margin': '10px', 'display': 'block'}
            )
        ], style={
            'backgroundColor': '#f8f9fa',
            'padding': '20px',
            'borderRadius': '8px',
            'marginBottom': '20px',
            'border': '1px solid #e9ecef'
        }),
        
        dcc.Graph(
            id='sales-chart',
            style={'height': '500px'}
        )
    ], style={
        'maxWidth': '1200px',
        'margin': '0 auto',
        'padding': '20px',
        'backgroundColor': '#ffffff'
    })
], style={
    'backgroundColor': '#ecf0f1',
    'minHeight': '100vh',
    'fontFamily': 'Arial, sans-serif'
})

# Callback to update chart based on region selection
@app.callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value')
)
def update_chart(selected_region):
    # Filter data based on selection
    if selected_region == 'all':
        filtered_df = df
        title = 'Pink Morsel Sales Over Time - All Regions'
    else:
        filtered_df = df[df['region'] == selected_region]
        title = f'Pink Morsel Sales Over Time - {selected_region.title()} Region'
    
    # Create the figure
    fig = px.line(
        filtered_df,
        x='date',
        y='sales',
        title=title,
        labels={'date': 'Date', 'sales': 'Sales ($)'},
        color_discrete_sequence=['#3498db']
    )
    
    # Update layout for better styling
    fig.update_layout(
        title_font_size=18,
        title_font_color='#2c3e50',
        plot_bgcolor='#f8f9fa',
        paper_bgcolor='white',
        font_family='Arial, sans-serif'
    )
    
    fig.update_xaxes(
        gridcolor='#e1e8ed',
        title_font_color='#34495e'
    )
    
    fig.update_yaxes(
        gridcolor='#e1e8ed',
        title_font_color='#34495e'
    )
    
    return fig

if __name__ == "__main__":
    app.run(debug=True)