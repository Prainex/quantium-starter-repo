import pytest
from dash.testing.application_runners import import_app
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def test_header_present(dash_duo):
    """Test that the header is present on the page"""
    # Import the app
    app = import_app("main")
    
    # Start the app
    dash_duo.start_server(app)
    
    # Check that the header element exists
    dash_duo.wait_for_element("h1", timeout=4)
    
    # Verify the header text
    header = dash_duo.find_element("h1")
    assert "Soul Foods — Pink Morsel Sales Visualiser" in header.text

def test_visualization_present(dash_duo):
    """Test that the chart visualization is present"""
    # Import the app
    app = import_app("main")
    
    # Start the app
    dash_duo.start_server(app)
    
    # Wait for the graph component to load
    dash_duo.wait_for_element("#sales-chart", timeout=4)
    
    # Check that the graph element exists
    graph_element = dash_duo.find_element("#sales-chart")
    assert graph_element is not None

def test_region_picker_present(dash_duo):
    """Test that the region picker radio buttons are present"""
    # Import the app
    app = import_app("main")
    
    # Start the app
    dash_duo.start_server(app)
    
    # Wait for the region filter to load
    dash_duo.wait_for_element("#region-filter", timeout=4)
    
    # Check that the radio button container exists
    region_filter = dash_duo.find_element("#region-filter")
    assert region_filter is not None
    
    # Check that all radio button options are present
    radio_inputs = dash_duo.find_elements("input[type='radio']")
    assert len(radio_inputs) == 5  # Should have 5 radio buttons (all, north, east, south, west)
    
    # Verify the labels are present
    labels = dash_duo.find_elements("label")
    label_texts = [label.text for label in labels if label.text.strip()]
    expected_labels = ["All Regions", "North", "East", "South", "West"]
    
    for expected_label in expected_labels:
        assert any(expected_label in text for text in label_texts)