let deleteBtns = document.querySelectorAll(".delete_item");
if (deleteBtns) {
  deleteBtns.forEach((node) =>
    node.addEventListener("click", function delete_item(event) {
      let productName =
        node.parentNode.parentNode.children[1].firstElementChild.innerHTML;
      let endpoint = "http://127.0.0.1:8000/cart/" + productName + "/delete";
      fetch(endpoint, {
        method: "GET",
      }).then(node.parentNode.parentNode.remove());
    })
  );
}
