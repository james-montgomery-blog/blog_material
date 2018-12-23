# Time_Series_Modeling

What is this course about? Working in data science at a financial institution, I cam to realise that there are a plethora of sequence and time series problems that would be valuable to solve but that many data scientist just don't know how to approach (myself included). Many data scientists resorted to the old "well I'm sure an lstm will work" approach...but that puts a bad taste in my mouth. Our job is to think and understand, not spam the keras api hoping to get decent results.

So, I spent a lot of time reading and trying to implement various online tutorials and research papers on time series modeling. This course is a collection of (mostly) other people's tutorials, but refactored to work together and provide a more holistic view of time series modeling than any one of these myriad of tutorials did originally. I've rewritten extensive portions of many of these tutorials and I apologize for any errors I may have accidentally introduced. I try to provide links or references to any and all resources I borrowed from to create this course in the sections where I reference said material.

All of the content is stored in Jupyter Notebooks. I recommend downloading the content locally. This will let you play with the code and actually run the examples for yourself.

I'd like to give a big thanks to Tom Caputo, who in every way started me on my journey to learn time series modeling as well as Kip Johnson and David Lutz who showed me the importance of giving back to the education of the data science community when I began my journey into data science. A special thanks to Jason Wittenbach who is probably the most knowledgable person I have ever met at Capital One and who I have bugged with more questions about modeling than Google itself.

Another (final) extra big thanks to Kate Highnam, whom without this tutorial would be considerably less comprehensible and much more boring.

I've set up a number of examples and homework problems to work through in this course, but if you find yourself needing more practice with the concepts discussed in this lecture series, try playing with these datasets:

[UCR Time Series Classification Archive](http://www.cs.ucr.edu/~eamonn/time_series_data/)

[Stata Press](http://www.stata-press.com/data/r15/ts.html)

### **Table of Contents:**

**Chapter One: Forecasting**

Part One:

* Who is this lecture for?
* What is a time series?
* Deconstructing a time series
  * The four basic components
  * Assumptions about the four components
  * Autocorrelation
  * Partial autocorrelation

Part Two:

* Starting simple
  * Rolling means
  * Single exponential smoothing
  * Double exponential smoothing
  * Triple exponential smoothing
* Moving to ARIMAs
  * Auto-regressive models
  * Moving average models
  * ARIMA models
  * Seasonal ARIMA models
  * Choosing values for p,d,q
* Wrap up

Part Three:

* Using what we've learned
* Homework

Part Four:

* Heteroscedasticity
* ARCH
* GARCH
* Using What We've Learned

Part Five:

* Multi-series models
* VAR
* VARMA
* How far we've come

Part Six:

* Bayesian parameter estimation

Part Seven:

* Dynamic factor models

Part Eight:

* Back to basics with filters
* Hodrick-Prescott filter
* Baxter-King approximate band-pass filter
* Christiano-Fitzgerald approximate band-pass filter

Part Nine: (Coming Soon)

* Deep Learning and Time Series
* Simple Neural Nets
* RNNs
* LSTMs

Part Ten: (Coming Soon)
* Adding Uncertainty to Deep Models
* Gaussian Processes

**Chapter Two: Anomaly Detection**

Part One:

* Anomaly Detection
* Common Series
* CUSUM

Part Two:

* Markov switching autoregression models

Part Three: (Coming Soon)

* Predictive models and anomaly detection

**Chapter Three: Time Sensitivity**

Part One: (Coming Soon)

* Stochastic Volatility Model
  * linear example
  * neural net example

Part Two: (Coming Soon)

* Gaussian Process (simple)
