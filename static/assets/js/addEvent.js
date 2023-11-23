function createDropdown() {
                        // Get the selected number of cats
                        var numberOfCats = document.getElementById("workhand_category").value;
                    
                        // Get the container div
                        var catContainer = document.getElementById("catContainer");
                        var mydivContainer = document.getElementById("mydiv");
    
                        // Clear previous content
                        catContainer.innerHTML = "";
                        mydivContainer.innerHTML = "";
                    
                        // Create a dropdown list
                            for (var i = 1; i <= numberOfCats; i++) {
                        
                                var dropdown = document.createElement("select");
                                dropdown.id = "catDropdown"+i;
                                dropdown.className = "form-item";
                                dropdown.name = "Workhand_categorie"
                                dropdown.style = "max-width:100%; background-color: #f7f7f7; border-color: #f0f0f0 ";

                                var textbox = document.createElement("input");
                                textbox.type = "text";
                                textbox.id = "catTextbox"+i;
                                textbox.name = "workhand_number"
                                textbox.className = "form-item p-2";
                                textbox.style = "max-width:100%; background-color: #f7f7f7; border-color: #f0f0f0 "
                                textbox.required = true;
                                
                                var option = document.createElement("option");
                                option.value = "";
                                option.text ="Choose Workhand Category";
                                dropdown.appendChild(option);

                                {% for i in Workhand_category %}
                                var option = document.createElement("option");
                                option.value = {{i.id}};
                                option.text ="{{i.workhand_category_name}}";
                                dropdown.appendChild(option);
                                {% endfor %}

                                // Append the dropdown and textbox to the container
                                catContainer.appendChild(dropdown);
                                mydivContainer.appendChild(textbox);
                            }
                        }