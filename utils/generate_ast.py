import sys
from pathlib import Path
from io import TextIOWrapper


def transform_param_from_c_style_to_python(param: str):
    param_type = param.split(" ")[0]
    param_name = param.split(" ")[1]

    return f"{param_name}: {param_type}"


def define_type(file: TextIOWrapper, base_name: str, class_name: str, fields: str):
    fields_list = fields.split(", ")
    params = ", ".join(map(transform_param_from_c_style_to_python, fields_list))

    # Constructor
    file.write(
        f"""class {class_name}({base_name}):

    def __init__(self, {params}):    
"""
    )

    # Store parameters in fields
    for field in fields_list:
        name = field.split(" ")[1]
        file.write(f"        self.{name} = {name}\n")


def define_ast(output_dir: str, base_name: str, types: list[str]):
    path = Path(output_dir) / f"{base_name.lower()}.py"

    with open(path.absolute(), "w") as file:
        file.write(
            f"""from abc import ABC

from pylox.token import Token


class {base_name}(ABC):
    pass


"""
        )

        for i, expr_type in enumerate(types):
            class_name = expr_type.split(":")[0].strip()
            fields = expr_type.split(":")[1].strip()
            define_type(file, base_name, class_name, fields)
            if i < len(types) - 1:
                file.write("\n\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: generate_ast <output_directory>")
        sys.exit(64)

    output_dir = sys.argv[1]

    define_ast(
        output_dir,
        "Expr",
        [
            "Binary   : Expr left, Token operator, Expr right",
            "Grouping : Expr expression",
            "Literal  : object value",
            "Unary    : Token operator, Expr right",
        ],
    )
