
user_name = "Alex"
is_active = True

if is_active:
    message = "welcome to python!"
    print(message);
print("outside if block:", {message});

print("*******Python Objects / Dictionaries ********")

frontend_dev = {
    "name": "Alex",
    "age": "22",
    "education": "Alevels"
}

print("name:", frontend_dev.get("name", "age" ));

for person, details in frontend_dev.items():
    print({person}, {details});

    dict1 = {"a": 1, "b": 2}
dict2 = {"b": 99, "c": 4}

# Merges into a new dictionary (right side overwrites duplicates)
merged = dict1 | dict2  
# Output: {'a': 1, 'b': 99, 'c': 4}
print("merged:", merged)

removedEl = frontend_dev.pop("name");
print("removed element:", removedEl);

frontend_dev.update({"age": "40"});
print('updated Element:', frontend_dev["age"]);

frontend_dev["name"] = "Peter";

print('Name:', frontend_dev["name"]);

print("name: ",frontend_dev.get("name", "age"));
print(f"object: {frontend_dev}")

print(frontend_dev)

print(f"*************Python Lists********")

technologies = ["vue", "react", "angular", "next", "rust", "python"];

print(f"indices: {technologies[1:4]}")
print(f"first element: {technologies[0:1]}")

copiedTechnologies = technologies[:]
print(f"copy: {copiedTechnologies}")
print(f"original: {technologies}")

copiedTechnologies.insert(1, "grail")
print(f"modified copy: {copiedTechnologies}")
print(f"original copy: {technologies}")

copiedTechnologies.append("java")
copiedTechnologies.insert(2, "typescript")

technologies.extend(copiedTechnologies)

print(f'original list: {technologies}');
print(f'copied list: {copiedTechnologies}');





