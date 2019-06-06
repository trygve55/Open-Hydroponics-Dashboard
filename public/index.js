function set_gpio(state) {
   fetch('/api/gpio', {
    method: 'POST',
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({state: state})
  }).then(
    response => response.json() // if the response is a JSON object
  ).then(
    response => console.log(response)
  ).catch(
    error => console.log(error) // Handle the error response object
  );
}