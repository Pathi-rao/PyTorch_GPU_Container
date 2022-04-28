## command to build the container:

`docker build -f Dockerfile -t "name_of_container" . `

(dot reprents the file is in same directory)

#### name of the container: siamese_docker_container
## to build without cashe add --> --no-cache

## To go inside the container:
`docker run -ti "name_of_container" /bin/bash` (this will activate the container)

## Nvidia toolkit must be installed in host machine (only once) inorder to use gpus. Once installed, run the container by specifying the gpus
`docker run --gpus 1 -ti siamese_docker_container /bin/bash`

## OR

`docker run --name <container_name> --gpus all -it <image_name>`

and

`nvidia-smi`

## Once the container is created, it installs conda and creates an env. Currently the env name is set to "siamese_conda_env". To activate it,

`conda activate siamese_conda_env`  or
`source activate siamese_conda_env`

## to check if everything is working as intended, go into src and run a test script

`cd src`

`python test.py`


## We need to mount data dir and dir where the results will be saved
`docker run -v <absolute_data_folder_path_in_localmachine>:/root/processed_data -ti <container_name> /bin/bash`

`docker run -v <absolute_resultsfolderpath_in_localmachine>:/root/docker_saved_data -ti <container_name> /bin/bash`
