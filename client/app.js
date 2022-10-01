let key;

function login(username, password) {
  var myHeaders = new Headers();
  myHeaders.append("Content-Type", "application/json");

  var raw = JSON.stringify({
    username: username,
    password: password,
  });

  var requestOptions = {
    method: "POST",
    headers: myHeaders,
    body: raw,
    redirect: "follow",
  };

  fetch("http://127.0.0.1:8000/users/login/", requestOptions)
    .then((response) => response.json())
    .then((data) => {
      key = data.key;
      console.log(key);
    })
    .catch((error) => console.log("error", error));
}

login("alisan6", "qazqwe123");
