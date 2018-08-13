# Change Log
<!--
All notable changes to the "faker-snippets" extension will be documented in this file.

Check [Keep a Changelog](http://keepachangelog.com/) for recommendations on how to structure this file.
-->
<!--
## [Unreleased]
-
-->
## [1.2.0] - 2018-08-13
### Added
- Faker::NationalHealthService
- Faker::SouthAfrica
- Faker::Buffy
- Faker::BojackHorseman
- Faker::GratefulDead
- Faker::IDNumber
    - spanish_citizen_number
    - spanish_foreign_citizen_number
    - south_african_id_number
    - valid_south_african_id_number
    - invalid_south_african_id_number
- Faker::SouthPark
- Faker::DcComics

### Changed
- Faker::Internet.user_name to Faker::Internet.username

### Removed
- Faker::Time.between(3.hours.ago, Time.now, :between)
- Faker::Cannabis.website

## [1.1.0] - 2018-07-07
### Added
- Faker::Name.female_first_name
- Faker::Bank.account_number
- Faker::Bank.routing_number
- Faker::WorldCup.stadium
- Faker::WorldCup.city
- Faker::Ethereum.address
- Faker::GreekPhilosophers

## [1.0.1] - 2018-06-17
### Added
- Index on readme for easier searching
- Script inside `scripts/sync.sh` to initiate faker submodule

### Changed
- Updated `generate.py` script to generate the index
- Updated `generate.py` script to write directly on `snippets.json` and `README.md` files

## [1.0.0] - 2018-06-14
### Added
- Faker Gem as a git submodule
- Released stable version

### Changed
- Doc's folder now inside `scripts/faker/doc`

### Removed
- Old `scripts/doc` folder

## [0.2.0] - 2018-03-16
### Added
- Short form snippets
- Usage gif

## [0.1.0] [0.1.1] [0.1.2] - 2018-03-08
- Added icon
- Added install instructions

## [0.0.1]
- Initial release
