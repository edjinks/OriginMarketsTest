# OriginMarketsTest

My implementation of the Backend Python Technical Test.<br>

This was my first time using Django and took me around 4 hours to complete.<br>

<h2>FEATURES:</h2>
<ul>
<li>login/logout functionality to limit users to only being able to see their own bonds</li>
<li>Users currently setup are: <br>
<ul>
 <li> U: admin, P: admin</li>
  <li> U: testuser, P: originmarkets</li>
 </ul></li>
<li>Filter by legalname (e.g http://127.0.0.1:8000/bonds/?legal_name=BNP PARIBAS)</li>
 <li>Automatically gather Legal Name from the GLEIF API on POST</li>
</ul>
 
<h2>PAGES:</h2>
<ul>
<li>http://127.0.0.1:8000/bonds</li>
<li>http://127.0.0.1:8000/admin</li>
<li>http://127.0.0.1:8000/accounts/login</li>
<li>http://127.0.0.1:8000/logout</li>
</ul>
