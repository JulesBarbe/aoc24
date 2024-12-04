use std::fs;
use regex::Regex;

fn problem1(program: &str) -> i32 {
    let re = Regex::new(r"mul\([0-9]{1,3},[0-9]{1,3}\)").unwrap();
    return re
        .find_iter(program)
        .map(|mul| {
            let cleaned = mul
                .as_str()
                .trim_start_matches("mul(")
                .trim_end_matches(")");
            let mut nums = cleaned.split(",")
                .map(|num| num.parse::<i32>().unwrap());
            nums.next().unwrap() * nums.next().unwrap()
        })
        .sum();
}

fn problem2(program: &str) -> i32 {
    let re = Regex::new(r"mul\([0-9]{1,3},[0-9]{1,3}\)|do\(\)|don't\(\)").unwrap();
    let acc: Vec<i32> = vec![1, 0];
    return re
        .find_iter(program)
        .fold(acc, |mut acc, x| {
            if x.as_str() == "do()" {
                acc[0] = 1;
                return acc;
            }
            else if x.as_str() == "don't()" {
                acc[0] = 0;
                return acc;
            }
            if acc[0] == 0 {
                return acc;
            }
            else {
                let cleaned = x
                    .as_str()
                    .trim_start_matches("mul(")
                    .trim_end_matches(")");
                let mut nums = cleaned.split(",")
                    .map(|num| num.parse::<i32>().unwrap());
                acc[1] += nums.next().unwrap() * nums.next().unwrap();
                return acc;
            }

        })
        .iter().as_slice()[1];

    
}

fn main() {
    let contents = fs::read_to_string("day3.txt").unwrap();
    println!("{}", problem1(&contents));
    println!("{}", problem2(&contents));
}
