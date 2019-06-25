- Moonchang Chae 님, hojel님 코드를 기반으로 수정함.
- SJVA, Plex plugin, 일반 python 공용으로 사용
- 쉘 사용법
~~~
usage: smi2srt_handle.py [-h] [--remake] [--no_remove_smi] [--no_append_ko]
                         [--no_change_ko_srt]
                         [--fail_move_path FAIL_MOVE_PATH]
                         work_path

SMI to SRT

positional arguments:
  work_path             디렉토리나 파일

optional arguments:
  -h, --help            show this help message and exit
  --remake              srt 파일이 있는 경우에도 재생성. (생략시 패스)
  --no_remove_smi       변환 후 smi 파일을 삭제하지 않음. (생략시 삭제)
  --no_append_ko        파일명에 ko 등을 추가하지 않음. (생략시 추가)
  --no_change_ko_srt    .srt 파일을 .ko.srt로 변경하지 않음. (생략시 변경함)
  --fail_move_path FAIL_MOVE_PATH
                        실패시 이동할 폴더. (생략시 이동하지 않음)
~~~                    



Convert subtitles in SMI to SRT
========================================

Plex agents to convert subtitles in SMI format to SRT format.

It demultiplex first if multiple language sections exist,
and then convert Korean section to SRT format.

TODO
-------------

* Support saving in ASS format
* Handling SMI file which has no language info header

Acknowledge
-------------

* [smi2srt](https://gist.github.com/suapapa/1532257)
