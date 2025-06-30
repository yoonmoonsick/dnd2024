#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Type_Name; 형식의 데이터를 Name 기준으로 정렬하는 알고리즘
"""

import sys

def process_data(input_string):
    """
    Type_Name; 형식의 데이터를 처리하는 메인 함수
    
    작업1: '_'을 구분자로 Type과 Name으로 분해
    작업2: Name을 기준으로 오름차순 정렬
    작업3: Type_Name 형식으로 재조립
    작업4: ';'를 구분자로 하여 최종 문자열 생성
    """
    
    # 입력 문자열에서 마지막 세미콜론 제거 및 공백 제거
    input_string = input_string.strip().rstrip(';')
    
    # 작업1: ';'로 분할하여 각 항목을 Type과 Name으로 분해
    items = []
    for item in input_string.split(';'):
        item = item.strip()
        if '_' in item:
            type_part, name_part = item.split('_', 1)  # 첫 번째 '_'로만 분할
            items.append((type_part, name_part))
        else:
            # '_'가 없는 경우 처리 (예외 상황)
            items.append(('', item))
    
    # 작업2: Name(두 번째 요소) 기준으로 오름차순 정렬
    sorted_items = sorted(items, key=lambda x: x[1])
    
    # 작업3: Type_Name 형식으로 재조립
    reassembled_items = []
    for type_part, name_part in sorted_items:
        if type_part:  # Type이 있는 경우
            reassembled_items.append(f"{type_part}_{name_part}")
        else:  # Type이 없는 경우
            reassembled_items.append(name_part)
    
    # 작업4: ';'를 구분자로 하여 최종 문자열 생성
    result = ';'.join(reassembled_items)
    
    return result

def main():
    """메인 함수 - 명령행 인자 또는 표준 입력에서 데이터를 받아 처리"""
    try:
        # 명령행 인자가 있는 경우 사용
        if len(sys.argv) > 1:
            input_data = sys.argv[1].strip()
        else:
            # 명령행 인자가 없으면 표준 입력에서 읽기
            input_data = input().strip()
        
        # 빈 입력 처리
        if not input_data:
            print("", end="")
            return
        
        # 데이터 처리
        result = process_data(input_data)
        
        # 표준 출력으로 결과 출력
        print(result, end="")
        
    except EOFError:
        # 입력이 없는 경우
        print("", end="")
    except Exception as e:
        # 오류 발생 시 stderr로 출력
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()