from main import app


def test_header_exists(dash_duo):
    """Test that the header is present on the page"""
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)
    
    # Verify the header text
    header = dash_duo.find_element("h1")
    assert "Soul Foods — Pink Morsel Sales Visualiser" in header.text


def test_visualization_exists(dash_duo):
    """Test that the chart visualization is present"""
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-chart", timeout=10)
    
    # Check that the graph element exists
    graph_element = dash_duo.find_element("#sales-chart")
    assert graph_element is not None


def test_region_picker_exists(dash_duo):
    """Test that the region picker radio buttons are present"""
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-filter", timeout=10)
    
    # Check that the radio button container exists
    region_filter = dash_duo.find_element("#region-filter")
    assert region_filter is not None
    
    # Check that radio button options are present
    radio_inputs = dash_duo.find_elements("input[type='radio']")
    assert len(radio_inputs) == 5  # Should have 5 radio buttons (all, north, east, south, west)