from time import sleep

import pytest

from yadiskdel import YaDiskDel


def test_createdir():
    # Добавьте свой токен
    token = ''
    ya = YaDiskDel(token)
    path = "dir_for_test"
    assert not (ya.dirinfo(path) == 200), "тест не возможен, папка существует"
    sleep(1)
    result = ya.createdir(path)
    assert result == 201, f"Error createdir status code = {result}"
    sleep(1)
    assert ya.dirinfo(path) == 200, f"Error dirinfo status code = {result}"
    sleep(1)
    res = ya.deletedir(path)
    assert res in [204, 202, 200], f"Error dir do not delete status code = {result}"


if __name__ == '__main__':
    pytest.main()