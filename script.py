import bpy

clipboard_data = bpy.context.window_manager.clipboard
new_names = clipboard_data.strip().splitlines()

obj = bpy.context.object

if obj and obj.data.shape_keys:
    shape_keys = obj.data.shape_keys.key_blocks
    total_keys = len(shape_keys)

    num_to_rename = min(len(new_names), total_keys - 1)

    for i in range(1, num_to_rename + 1):
        index = total_keys - i  
        old_name = shape_keys[index].name
        new_name = new_names[-i]  
        shape_keys[index].name = new_name
        print(f"Renamed: {old_name} -> {new_name}")

    if len(new_names) < total_keys - 1:
        print(f"Skipped {total_keys - 1 - len(new_names)} shape key(s) at the top.")
else:
    print("No shape keys found on selected object.")
