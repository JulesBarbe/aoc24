use std::fs;

fn problem1(reports: &[&str]) {
    let count = reports
        .iter()
        .filter(|report| {
            let levels: Vec<i32> = report
                .split_whitespace()
                .map(|x| x.parse::<i32>().unwrap())
                .collect();
            let inc = levels[1] > levels[0];
            let diff = (levels[1] - levels[0]).abs();
            if diff < 1 || diff > 3 {
                return false;
            }
            levels
                .windows(2)
                .all(|pair: &[i32]| {
                    let diff = (pair[0] - pair[1]).abs();
                    let valid_diff = diff != 0 && diff <= 3;
                    let valid_dir = if inc {
                        pair[1] > pair[0]
                    } else {
                        pair[1] < pair[0]
                    };
                    valid_diff && valid_dir
                })
        })
        .count();
    println!("{}", count);
}

fn is_valid(levels: &[i32]) -> bool {
    if levels.len() < 2 {
        return false;
    }
    let inc = levels[1] > levels[0];
    let diff = (levels[0] - levels[1]).abs();
    if diff < 1 || diff > 3 {
        return false;
    }
    levels
        .windows(2)
        .all(|pair| {
            let diff = (pair[0] - pair[1]).abs();
            let valid_diff = diff != 0 && diff <= 3;
            let valid_dir = if inc {
                pair[1] > pair[0]
            } else {
                pair[1] < pair[0]
            };
            valid_diff && valid_dir
        })
}

fn problem2(reports: &[&str]) {
    let count = reports
        .iter()
        .filter(|report| {
            let levels: Vec<i32> = report
            .split_whitespace()
            .map(|x| x.parse::<i32>().unwrap())
            .collect();
            if is_valid(&levels) {
                return true;
            }
            (0..levels.len()).any(|j| {
                let mut subarray = levels.clone();
                subarray.remove(j);
                return is_valid(&subarray);
            })
        })
        .count();
    println!("{}", count);
}

fn main() {
    let contents = fs::read_to_string("day2.txt").unwrap();
    let lines = contents.lines().collect::<Vec<&str>>();
    problem1(&lines);
    problem2(&lines);
}
