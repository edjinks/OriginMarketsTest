# OriginMarketsTest

My implementation of the Backend Python Technical Test.<br>

This was my first time using Django and took me around 4 hours to complete.<br>

<h2>FEATURES:</h2>
login/logout functionality to limit users to only being able to see their own bonds<br>
Users currently setup are: <br>
<ul>
 <li> U: admin, P: admin;</li>
  <li> U: testuser, P: originmarkets</li></ul>
Filter by legalname (e.g http://127.0.0.1:8000/bonds/?legal_name=BNP PARIBAS)<br>
Automatically gather Legal Name from the GLEIF API on POST

 
<h2>PAGES:<\h2>
http://127.0.0.1:8000/bonds
http://127.0.0.1:8000/admin
http://127.0.0.1:8000/accounts/login
http://127.0.0.1:8000/logout

