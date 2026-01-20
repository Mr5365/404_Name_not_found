import trimesh

input_ply = "colmap_workspace/sparse/model.ply"
output_glb = "colmap_workspace/sparse/model.glb"

# Load sparse point cloud WITHOUT processing
cloud = trimesh.load(input_ply, process=False)

# Create a scene (important for point clouds)
scene = trimesh.Scene()
scene.add_geometry(cloud)

# Export to GLB
scene.export(output_glb)

print("✅ Point-cloud GLB created successfully")
