<h1>Fun Fact Generator</h1>
<h3>Fun Fact Generator in Python: https://www.geeksforgeeks.org/fun-fact-generator-web-app-in-python/amp/</h3>

<ul>
  <li>Import all the required modules</li>
  <li>Send <b>GET</b> requests with the <b>requests.request()</b> method, and use the json.loads() function to parse a valid <b>JSON</b> message and transform it to a Python Dictionary. Since the <b>requests function</b> will create a dictionary of items, and we only need text, so we will pass <b>response.text</b> inside the json module.</li>
  <li>Now, because we need the text, i.e. Facts, we will pass the text within the <b>data list</b> and print the facts using the <b>style</b> function defined in the <b>pywebio</b> module. Because data is a dictionary of random jokes involving several useless items, we will just get the text section.</li>
</ul>
