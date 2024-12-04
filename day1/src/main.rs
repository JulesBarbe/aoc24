use std::fs;
use std::collections::{HashMap, HashSet};

fn problem1(lines: &[&str]) {
    let (mut l1, mut l2): (Vec<i32>, Vec<i32>) = lines.iter()
        .map(|line| {
            let mut parts = line.split_whitespace()
                .map(|elem| elem.parse::<i32>().unwrap());
            (parts.next().unwrap(), parts.next().unwrap())
        })
        .unzip();
    l1.sort();
    l2.sort();
    let result: i32 = l1.iter()
                        .zip(l2.iter())
                        .map(|(x1, x2)| (x1 - x2).abs())
                        .sum();
    println!("{}", result);
}

fn problem2(lines: &[&str]) {
    let mut d: HashMap<i32, i32> = HashMap::new();
    let mut s: HashSet<i32> = HashSet::new();
    lines.iter().for_each(|line| {
        let mut parts = line.split_whitespace()
                                                 .map(|elem| elem.parse::<i32>().unwrap());
        let (l, r) = (parts.next().unwrap(), parts.next().unwrap());
        s.insert(l);
        *d.entry(r).or_insert(0) += 1;
    });

    let result: i32 = d.iter()
                       .filter(|(k, _)| s.contains(k))
                       .map(|(k, v)| k * v)
                       .sum();

    println!("{}", result);
}

fn main() {
    let contents = fs::read_to_string("day1.txt").expect("File should be readable");
    let lines = contents.lines().collect::<Vec<&str>>();
    problem1(&lines);
    problem2(&lines);
}
            
                                