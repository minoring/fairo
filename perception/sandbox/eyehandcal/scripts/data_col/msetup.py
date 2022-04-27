import mrp 


mrp.process(
    name="take_picture",
    runtime=mrp.Conda(
        channels = ["fair-robotics", "conda-forge"],
        dependendices = ["python>=3.7", 
        "pyusb", 
        "numpy", 
        "librealsense", 
        "pycapnp", 
        {"pip" : [ "alephzero"]}],
        run_command = ["python", "take_picture.py"]
        )
    )

mrp.process(
    name="take_pose",
    runtime=mrp.Conda(
        channels = ["pytorch",
            "fair-robotics",
            "aihabitat",
            "conda-forge"],
        dependendices = ["python>=3.7", 
        "scipy",
        "polymetis=874",
        {"pip" : [ "alephzero"]}],
        run_command = ["python", "take_pose.py"]
        )
)

mrp.process(
    name="traj_col",
    runtime=mrp.Conda(
        channels = ["pytorch",
            "fair-robotics",
            "aihabitat",
            "conda-forge"],
        dependendices = ["python>=3.7", 
        "pickle",
        {"pip" : [ "alephzero"]}],
        run_command = ["python", "traj_col.py"]
        )
)
mrp.main()