const btns = document.querySelectorAll("#casa1");
for (const btn of btns) {
  btn.addEventListener("click", function (e) {
    e.preventDefault();
  
    let id = this.value;
    console.log(id);

    axios.get("http://127.0.0.1:8000/api/user/" + id).then(
      (response) => {
        console.log(response.data); // response.data ya es un JSveON
        document.querySelector("#id2").value = response.data["id"]
        document.querySelector("#name2").value = response.data["nombres"];
        document.querySelector("#apellidos2").value = response.data["apellidos"];
        document.querySelector("#password2").value= "Encrypt";

        console.log(nombres);
      },
      (error) => {
        console.log(error);
      }
    );
  });
}

// document.querySelector("#insertar").addEventListener("click", (e)=>{
// e.preventDefault();
// const nom = document.querySelector("#name").value;
// const ape = document.querySelector("#apellidos").value;
// const pass= document.querySelector("#password").value;

// axios({
//   method: 'post',
//   url: 'http://127.0.0.1:8000/api/user',
//   data: {
//     id:"1",
//     nombres:nom,
//     apellidos:ape,
//     password:pass,
//     fecha:"12/05/2023"
//   }
// }).then((response) => {
//   console.log(response);
// }, (error) => {
//   console.log(error);
// });
// });
