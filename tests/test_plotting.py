from resumeanalyser.plotting import plot_wordcloud
from resumeanalyser.plotting import plot_topwords
from resumeanalyser.plotting import plot_suite
from matplotlib.testing.decorators import image_comparison
import numpy as np
import pytest

test_text = 'I am going to fill in a test text here the the the a a a a'
### Edge Case Error Raising
def test_plot_wordcloud_edge_error():
    with pytest.raises(ValueError):
        plot_wordcloud("")
    with pytest.raises(ValueError):
        plot_wordcloud(None)
    with pytest.raises(TypeError):
        plot_wordcloud(999)

def test_plot_topwords_edge_error():
    with pytest.raises(ValueError):
        plot_topwords("")
    with pytest.raises(ValueError):
        plot_topwords(None)
    with pytest.raises(TypeError):
        plot_topwords(999)
    with pytest.raises(ValueError):
        plot_topwords(test_text,1)

def test_plot_suite_edge_error():
    with pytest.raises(ValueError):
        plot_suite("")
    with pytest.raises(ValueError):
        plot_suite(None)
    with pytest.raises(TypeError):
        plot_suite(999)
    with pytest.raises(ValueError):
        plot_topwords(test_text,'2')
    with pytest.raises(ValueError):
        plot_topwords(test_text,0)

### Image Comparison Test
@image_comparison(baseline_images=['img_wordcloud'], remove_text=True,
                  extensions=['png'], style='mpl20')
def test_plot_wordcloud_with_text():
    plot_wordcloud(test_text)

@image_comparison(baseline_images=['img_topwords'], remove_text=True,
                  extensions=['png'], style='mpl20')
def test_plot_topwords_with_text():
    plot_topwords(test_text)

@image_comparison(baseline_images=['img_suite'], remove_text=True,
                  extensions=['png'], style='mpl20')
def test_plot_suite_with_text():
    plot_suite(test_text)

### Type matching Test
def test_plot_wordcloud_type():
    assert str(type(plot_wordcloud(test_text)))=="<class 'matplotlib.image.AxesImage'>", "plot_wordcloud Output Not Correct."

def test_plot_topwords_type():
    assert str(type(plot_topwords(test_text)))=="<class 'matplotlib.container.BarContainer'>", "plot_topwords Output Not Correct."

def test_plot_suite_with_type():
    assert str(type(plot_suite(test_text)))=="<class 'matplotlib.figure.Figure'>", "plot_suite Output Not Correct."

### Plot Detail Test
##### plot_wordcloud
def test_plot_wordcloud_pixels():
    assert np.isclose(plot_wordcloud(test_text).get_array().mean(), 25.8546316), "plot_wordcloud Image pixels not Correct."

def test_plot_wordcloud_extent():
    assert plot_wordcloud(test_text).get_extent()==[-0.5, 799.5, 499.5, -0.5], "plot_wordcloud Image extent not Correct."

def test_plot_wordcloud_color():
    assert plot_wordcloud(test_text).cmap.name=='viridis', "plot_wordcloud Image color style not Correct."

def test_plot_wordcloud_shape():
    assert plot_wordcloud(test_text).get_shape() == (500, 800, 3), "plot_wordcloud Image shape not Correct."

##### plot_topwords      
def test_plot_topwords_data():
    assert np.isclose(plot_topwords(test_text).datavalues.mean(),1.6), "plot_topwords data Not Correct."

def test_plot_topwords_orientation():
    assert plot_topwords(test_text).orientation=='vertical', "plot_topwords orientation Not Correct."

def test_plot_topwords_bar_angle():
    assert plot_topwords(test_text).patches[0].angle==0, "plot_topwords bar angle Not Correct."

def test_plot_topwords_bar_height():
    assert plot_topwords(test_text).patches[0].get_height()==5, "plot_topwords bar height Not Correct."

##### plot_suite
def test_plot_suite_size():
    assert plot_suite(test_text).properties()['size_inches'].tolist()==[10.0, 5.0], "plot_suite size Not Correct."

def test_plot_suite_cloudtitle():
    assert plot_suite(test_text).properties()['axes'][0].title.get_text()=='WordCloud', "plot_suite worldcloud title Not Correct."

def test_plot_suite_bartitle():
    assert plot_suite(test_text).properties()['axes'][1].title.get_text()=='Top Frequency Words', "plot_suite barchart title Not Correct."

def test_plot_suite_barxlabel():
    assert plot_suite(test_text).properties()['axes'][1].get_xlabel()=='Word', "plot_suite barchart xlabel Not Correct."

def test_plot_suite_barylabel():
    assert plot_suite(test_text).properties()['axes'][1].get_ylabel()=='Count', "plot_suite barchart ylabel Not Correct."