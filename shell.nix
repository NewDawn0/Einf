{ pkgs ? import <nixpkgs> { } }:
let
  python-pkgs = ps: with ps; [ pandas scikit-learn matplotlib numpy ];
  python-ext = pkgs.python3.withPackages python-pkgs;
in python-ext.env
