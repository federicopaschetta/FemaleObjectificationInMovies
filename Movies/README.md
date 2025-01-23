Elenco del percorso delle cartelle per il volume TOSHIBA EXT
Numero di serie del volume: 0E8D-35B5
E:.
+---MG_annots
|   +---Annotations
|   |   +---py3loader
|   |   |   +---__pycache__
|   |   +---startend_frame
|   |       +---tt0073486
|   |---FaceTracks
|   |   +---mg_ftracks
|   |       +---ftracks
|   |       |   +---tt0073486
|   |       +---ftracks_ids
|   |---Shot_and_Scene
|   |   +---scene_boundaries
|   |   +---video_boundaries
|   +---Subtitles
|       +---clip_srt
|       |   +---tt0073486
|       +---full_srt
+---MG_movies --> Full movies in .MP4

1. Annotations
    - moves_list: list with IDs of movies
    - Movie_list.ipynb: file with script got from dvds_julie
    - dvds/dvds_julie: ID film, film name, publishing year, Amazon link
    - startend_frame: folder of images containing start and end frames of scenes -> only 'One Flew Over the Cuckoo's Nest'
    - py3loader: folder with scripts containing graph annotations

2. FaceTracks/mg_ftracks
    - ftracks: folder of JSON ftracks objects with following structure -> One Flew Over the Cuckoo's Nest
        - ftracks: list of sequence of frames with people inside (?) each with a list of objects inside with the structure:
            - timestamp: timestamp of the frame (?)
            - frame: frame number (?)
            - ftrack_id: ???
            - w	: width of the object
            - h	: height of the object
            - y	: y position of the object
            - x	: x position of the object
        - frame2ftracks: list of empty objects (when no people inside the screen?)
    - ftracks_ids -> list of people inside the frame in the scene (?)

3. Shot_and_scene
    - scene_boundaries/xx.scenes.gt: file with a list of x y z numbers
    - video_boundaries
        - xx.matidx: file with a list of x y numbers
        - xx.videvents: file with a list of x y CUT

4. Subtitles
    - clip_srt/xx: list of subtitles with a file for each scene with the following format:
        init_time --> end_time
        What the character is saying
        or
        - Character1 words
        - Character2 words

    - full_srt/xx: condensed version with only one file in the following format:
        num_sub
        init_time --> end_time
        What the character is saying
        or
        - Character1 words
        - Character2 words
    
