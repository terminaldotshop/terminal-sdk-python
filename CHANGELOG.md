# Changelog

## 1.12.2 (2025-06-30)

Full Changelog: [v1.12.1...v1.12.2](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.12.1...v1.12.2)

### Bug Fixes

* **ci:** correct conditional ([a97a328](https://github.com/terminaldotshop/terminal-sdk-python/commit/a97a3282115977827373a0715323d703ee21057b))


### Chores

* **ci:** only run for pushes and fork pull requests ([38bba09](https://github.com/terminaldotshop/terminal-sdk-python/commit/38bba09c0a0cb034ebfd599e742c33a906847cf7))

## 1.12.1 (2025-06-27)

Full Changelog: [v1.12.0...v1.12.1](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.12.0...v1.12.1)

### Bug Fixes

* **ci:** release-doctor — report correct token name ([2034cac](https://github.com/terminaldotshop/terminal-sdk-python/commit/2034cac9a93880e3904d713d9e07138fb656b3c7))


### Chores

* **tests:** skip some failing tests on the latest python versions ([d5a3c2d](https://github.com/terminaldotshop/terminal-sdk-python/commit/d5a3c2d7c53b3628e3a5678ee6d701f26976aeda))

## 1.12.0 (2025-06-21)

Full Changelog: [v1.11.1...v1.12.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.11.1...v1.12.0)

### Features

* **client:** add follow_redirects request option ([9bd4cf4](https://github.com/terminaldotshop/terminal-sdk-python/commit/9bd4cf4c4a8941ec67d8ef70a1a88d1c147c65e1))
* **client:** add support for aiohttp ([a21864c](https://github.com/terminaldotshop/terminal-sdk-python/commit/a21864cfba2db14411209bca5fd6276ac123b71e))


### Bug Fixes

* **client:** correctly parse binary response | stream ([67e114d](https://github.com/terminaldotshop/terminal-sdk-python/commit/67e114d0986fb2b09e2a21ffc8150c6cfa108fda))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([3a3a5a8](https://github.com/terminaldotshop/terminal-sdk-python/commit/3a3a5a88089f0e2f96eb34d8ad639d5db82f6f3b))


### Chores

* **ci:** enable for pull requests ([0b9c773](https://github.com/terminaldotshop/terminal-sdk-python/commit/0b9c773f7cba0360927423ebd82193c50d7d235a))
* **ci:** fix installation instructions ([c67fc25](https://github.com/terminaldotshop/terminal-sdk-python/commit/c67fc255b0d2a3bd250b469a01d5baccf8f4c5a6))
* **ci:** upload sdks to package manager ([c380e7e](https://github.com/terminaldotshop/terminal-sdk-python/commit/c380e7ef5adffca1e82bb10b99e9a9d4dfe8217a))
* **docs:** grammar improvements ([dff2776](https://github.com/terminaldotshop/terminal-sdk-python/commit/dff2776cc45b31111ce791f1d4632ebed17b5ac0))
* **docs:** remove reference to rye shell ([fb612e7](https://github.com/terminaldotshop/terminal-sdk-python/commit/fb612e76e759abdc355b4af1333fe5079f60cd50))
* **internal:** codegen related update ([858b047](https://github.com/terminaldotshop/terminal-sdk-python/commit/858b047b0765eae7915d38f716693bb13ac48876))
* **internal:** update conftest.py ([f211b5b](https://github.com/terminaldotshop/terminal-sdk-python/commit/f211b5b8ed1f93ee6ef1596133a5058962f28248))
* **readme:** update badges ([b9b68c0](https://github.com/terminaldotshop/terminal-sdk-python/commit/b9b68c07b61370f2c4fba011760e41179480f7a8))
* **tests:** add tests for httpx client instantiation & proxies ([87d9495](https://github.com/terminaldotshop/terminal-sdk-python/commit/87d94957188a9602e3d372510cd958f8d87985cf))
* **tests:** run tests in parallel ([2533b57](https://github.com/terminaldotshop/terminal-sdk-python/commit/2533b57e46766b33207ace1adcc1a46550bc7097))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([f2d5840](https://github.com/terminaldotshop/terminal-sdk-python/commit/f2d58408b719707774fc5cb099ce8cb48a749a2d))

## 1.11.1 (2025-05-10)

Full Changelog: [v1.11.0...v1.11.1](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.11.0...v1.11.1)

### Bug Fixes

* **package:** support direct resource imports ([b676099](https://github.com/terminaldotshop/terminal-sdk-python/commit/b67609908f07f26b9b951f531adb964e4c3bfea8))


### Chores

* **internal:** avoid errors for isinstance checks on proxies ([a61cacf](https://github.com/terminaldotshop/terminal-sdk-python/commit/a61cacf60150c76bbe3ede309300f7498c2be790))

## 1.11.0 (2025-04-24)

Full Changelog: [v1.10.0...v1.11.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.10.0...v1.11.0)

### Features

* **api:** global region, typed tracking status, variant tags ([55f97d3](https://github.com/terminaldotshop/terminal-sdk-python/commit/55f97d3481f9d81e4de4a4e4755e7440b1902f7a))
* **api:** product variant descriptions ([0e4a97d](https://github.com/terminaldotshop/terminal-sdk-python/commit/0e4a97d8dfbeda73b0b69d5bbeec380ffb57d0fc))


### Chores

* broadly detect json family of content-type headers ([db7288e](https://github.com/terminaldotshop/terminal-sdk-python/commit/db7288e1db9974ee578af88ced0a7174f3447d53))
* **ci:** only use depot for staging repos ([a293466](https://github.com/terminaldotshop/terminal-sdk-python/commit/a2934662486ff56f1407702557c2d7547b781254))
* **internal:** codegen related update ([7e42d70](https://github.com/terminaldotshop/terminal-sdk-python/commit/7e42d7065218f4d3795750c4155aef399b2ca37a))
* **internal:** minor formatting changes ([044e54a](https://github.com/terminaldotshop/terminal-sdk-python/commit/044e54a4f2f34bff972c54b4158ec10820d0d7ff))

## 1.10.0 (2025-04-23)

Full Changelog: [v1.9.0...v1.10.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.9.0...v1.10.0)

### Features

* **api:** include price on subscriptions ([641a792](https://github.com/terminaldotshop/terminal-sdk-python/commit/641a7922cd98a736c0afe6352b16aaea92973f96))


### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([79d90e5](https://github.com/terminaldotshop/terminal-sdk-python/commit/79d90e5f5a36569e3fd081b3cc600ed96315c937))


### Chores

* **ci:** add timeout thresholds for CI jobs ([a2d45d9](https://github.com/terminaldotshop/terminal-sdk-python/commit/a2d45d94a3a2018aaf7202786ea591d0e19a4e7a))
* **internal:** fix list file params ([e24aa62](https://github.com/terminaldotshop/terminal-sdk-python/commit/e24aa62985b91da5ea0add44e9832ae7dc085ac0))
* **internal:** import reformatting ([d7bc394](https://github.com/terminaldotshop/terminal-sdk-python/commit/d7bc3947496de2a8efcb6c4e8ee3f5f4ad386f4e))
* **internal:** refactor retries to not use recursion ([45f9f55](https://github.com/terminaldotshop/terminal-sdk-python/commit/45f9f553cf4a42ee709da2b8d215c31f30c04812))
* **internal:** update models test ([50a5d0b](https://github.com/terminaldotshop/terminal-sdk-python/commit/50a5d0b4ea8b4e21f55c2a073142b3329c010c63))

## 1.9.0 (2025-04-18)

Full Changelog: [v1.8.0...v1.9.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.8.0...v1.9.0)

### Features

* **api:** update subscription route ([d376b2b](https://github.com/terminaldotshop/terminal-sdk-python/commit/d376b2b47c6dcbdc8954a6070ab6ddb7a5f268b4))


### Chores

* **client:** minor internal fixes ([ea926ad](https://github.com/terminaldotshop/terminal-sdk-python/commit/ea926ad8d5a78d051e5da41d6ab14069b0a920bb))
* **internal:** base client updates ([b449e6a](https://github.com/terminaldotshop/terminal-sdk-python/commit/b449e6a9b006f27b002ce6468c9edda0e4efe313))
* **internal:** bump pyright version ([45eaad7](https://github.com/terminaldotshop/terminal-sdk-python/commit/45eaad7c82855c080157d4472c971815370cfabe))
* **internal:** update pyright settings ([aaf385b](https://github.com/terminaldotshop/terminal-sdk-python/commit/aaf385bc137e1239512014f81e5a4fc7eeb6a388))

## 1.8.0 (2025-04-14)

Full Changelog: [v1.7.0...v1.8.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.7.0...v1.8.0)

### Features

* **api:** include created timestamps ([dad128a](https://github.com/terminaldotshop/terminal-sdk-python/commit/dad128a2c454acc28fa505d049d8f610ab418230))


### Bug Fixes

* **perf:** optimize some hot paths ([8a11ed7](https://github.com/terminaldotshop/terminal-sdk-python/commit/8a11ed765f925233fc350e672a68a76f558a3356))
* **perf:** skip traversing types for NotGiven values ([1e7a1e3](https://github.com/terminaldotshop/terminal-sdk-python/commit/1e7a1e3e1e1166dbedf6013ff711b87d77cf9400))


### Chores

* **internal:** expand CI branch coverage ([349cb45](https://github.com/terminaldotshop/terminal-sdk-python/commit/349cb4525d2008c42c3b6ae39d841c950c6e5a91))
* **internal:** reduce CI branch coverage ([d88ec66](https://github.com/terminaldotshop/terminal-sdk-python/commit/d88ec6653de4e5aa2f2fed70957f3e397e1d7c38))

## 1.7.0 (2025-04-09)

Full Changelog: [v1.6.1...v1.7.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.6.1...v1.7.0)

### Features

* **api:** include shipment tracking info on order ([#116](https://github.com/terminaldotshop/terminal-sdk-python/issues/116)) ([194091b](https://github.com/terminaldotshop/terminal-sdk-python/commit/194091bc078214c61d6279b7214b0822d0183b1d))


### Chores

* **internal:** remove trailing character ([#113](https://github.com/terminaldotshop/terminal-sdk-python/issues/113)) ([11cab8a](https://github.com/terminaldotshop/terminal-sdk-python/commit/11cab8a5c20e0fdd59b94ea80947605bf29692e4))
* **internal:** slight transform perf improvement ([#115](https://github.com/terminaldotshop/terminal-sdk-python/issues/115)) ([dc6a830](https://github.com/terminaldotshop/terminal-sdk-python/commit/dc6a830cb0e5e05aa50f9c5313d618ac6d617c44))

## 1.6.1 (2025-04-02)

Full Changelog: [v1.6.0...v1.6.1](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.6.0...v1.6.1)

### Bug Fixes

* pluralize `list` response variables ([#111](https://github.com/terminaldotshop/terminal-sdk-python/issues/111)) ([efe4050](https://github.com/terminaldotshop/terminal-sdk-python/commit/efe40507ac770afbb37cc211c158a6e424e9100f))
* remove trailing / for environments ([#110](https://github.com/terminaldotshop/terminal-sdk-python/issues/110)) ([32e0d53](https://github.com/terminaldotshop/terminal-sdk-python/commit/32e0d531892d8429917e01ff391c5cd1ad4fe2dd))


### Chores

* fix typos ([#108](https://github.com/terminaldotshop/terminal-sdk-python/issues/108)) ([1a18e63](https://github.com/terminaldotshop/terminal-sdk-python/commit/1a18e634ec5758abef88a331a6fe9b56f431c8ac))

## 1.6.0 (2025-03-17)

Full Changelog: [v1.5.1...v1.6.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.5.1...v1.6.0)

### Features

* **api:** region model ([#97](https://github.com/terminaldotshop/terminal-sdk-python/issues/97)) ([07ff267](https://github.com/terminaldotshop/terminal-sdk-python/commit/07ff26716ee141b33a913c041a23f1b32aefd9ab))


### Bug Fixes

* **ci:** ensure pip is always available ([#104](https://github.com/terminaldotshop/terminal-sdk-python/issues/104)) ([07b0c98](https://github.com/terminaldotshop/terminal-sdk-python/commit/07b0c98365c3f90c3a8b075c3074ceb12e7bd709))
* **ci:** remove publishing patch ([#106](https://github.com/terminaldotshop/terminal-sdk-python/issues/106)) ([9c21943](https://github.com/terminaldotshop/terminal-sdk-python/commit/9c21943e996db21ec0e7f9b79f93fac80b9dde19))

## 1.5.1 (2025-03-15)

Full Changelog: [v1.5.0...v1.5.1](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.5.0...v1.5.1)

### Bug Fixes

* **types:** handle more discriminated union shapes ([#102](https://github.com/terminaldotshop/terminal-sdk-python/issues/102)) ([8879a51](https://github.com/terminaldotshop/terminal-sdk-python/commit/8879a51fe6b9ebd64192cc7217039ff14c4ac1db))


### Chores

* **internal:** bump rye to 0.44.0 ([#101](https://github.com/terminaldotshop/terminal-sdk-python/issues/101)) ([c381a8b](https://github.com/terminaldotshop/terminal-sdk-python/commit/c381a8bf59f7c035db408921ed352615e09d8493))
* **internal:** codegen related update ([#100](https://github.com/terminaldotshop/terminal-sdk-python/issues/100)) ([fa1bec3](https://github.com/terminaldotshop/terminal-sdk-python/commit/fa1bec32a61228b33398681d499d36713575245c))
* **internal:** remove extra empty newlines ([#98](https://github.com/terminaldotshop/terminal-sdk-python/issues/98)) ([dc37340](https://github.com/terminaldotshop/terminal-sdk-python/commit/dc373407e9725afda24896c5e79de7b6fb8b7822))

## 1.5.0 (2025-03-13)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.4.0...v1.5.0)

### Features

* **api:** region type ([#94](https://github.com/terminaldotshop/terminal-sdk-python/issues/94)) ([a5111bb](https://github.com/terminaldotshop/terminal-sdk-python/commit/a5111bbf6a338e6c154ddd25d38fe8d024168c70))

## 1.4.0 (2025-03-13)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.3.0...v1.4.0)

### Features

* **api:** add region to `GET /view/init` ([#91](https://github.com/terminaldotshop/terminal-sdk-python/issues/91)) ([2f0982d](https://github.com/terminaldotshop/terminal-sdk-python/commit/2f0982dba3b12696519fab909f83486a2052d21b))

## 1.3.0 (2025-03-13)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.2.0...v1.3.0)

### Features

* **api:** remove gift cards ([#88](https://github.com/terminaldotshop/terminal-sdk-python/issues/88)) ([423b013](https://github.com/terminaldotshop/terminal-sdk-python/commit/423b013385e2dad4ff60881bfea7ca3b023516c2))

## 1.2.0 (2025-03-13)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** clear cart api ([#85](https://github.com/terminaldotshop/terminal-sdk-python/issues/85)) ([27777a4](https://github.com/terminaldotshop/terminal-sdk-python/commit/27777a441938716d20ab7be85405ee81fc91120c))

## 1.1.0 (2025-03-11)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v1.0.0...v1.1.0)

### Features

* **api:** gift cards ([#83](https://github.com/terminaldotshop/terminal-sdk-python/issues/83)) ([2f579f2](https://github.com/terminaldotshop/terminal-sdk-python/commit/2f579f2cc2db07daa43cb9424f3d9891e062bed8))

## 1.0.0 (2025-03-07)

Full Changelog: [v0.1.0-alpha.14...v1.0.0](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.14...v1.0.0)

### Features

* **api:** manual updates ([#79](https://github.com/terminaldotshop/terminal-sdk-python/issues/79)) ([5d9c36b](https://github.com/terminaldotshop/terminal-sdk-python/commit/5d9c36bb699bbc09da33c6fff8b7d5277b56dedd))


### Chores

* **internal:** remove unused http client options forwarding ([#77](https://github.com/terminaldotshop/terminal-sdk-python/issues/77)) ([7abe7d0](https://github.com/terminaldotshop/terminal-sdk-python/commit/7abe7d0780a2308e319c3061208ab1bd97f0fbff))

## 0.1.0-alpha.14 (2025-02-28)

Full Changelog: [v0.1.0-alpha.13...v0.1.0-alpha.14](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.13...v0.1.0-alpha.14)

### Features

* **api:** manual updates ([#74](https://github.com/terminaldotshop/terminal-sdk-python/issues/74)) ([fdc1af1](https://github.com/terminaldotshop/terminal-sdk-python/commit/fdc1af14fce8c76d25fbcf480c2da9abc11b6b3d))

## 0.1.0-alpha.13 (2025-02-28)

Full Changelog: [v0.1.0-alpha.12...v0.1.0-alpha.13](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.12...v0.1.0-alpha.13)

### Features

* **api:** manual updates ([#71](https://github.com/terminaldotshop/terminal-sdk-python/issues/71)) ([9781030](https://github.com/terminaldotshop/terminal-sdk-python/commit/9781030c2eb00526f97ed957b28f91266b035ed3))


### Chores

* **docs:** update client docstring ([#70](https://github.com/terminaldotshop/terminal-sdk-python/issues/70)) ([da48dbf](https://github.com/terminaldotshop/terminal-sdk-python/commit/da48dbf4f04fd35d3844cf2d2a2c11f7bc451718))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#69](https://github.com/terminaldotshop/terminal-sdk-python/issues/69)) ([6cf439f](https://github.com/terminaldotshop/terminal-sdk-python/commit/6cf439f3f3b8cf38232c41e826db5dfb58042a70))

## 0.1.0-alpha.12 (2025-02-26)

Full Changelog: [v0.1.0-alpha.11...v0.1.0-alpha.12](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.11...v0.1.0-alpha.12)

### Features

* **api:** manual updates ([#66](https://github.com/terminaldotshop/terminal-sdk-python/issues/66)) ([9688e34](https://github.com/terminaldotshop/terminal-sdk-python/commit/9688e344bf7e1ec2380c6db3ab0b4e0f547428db))
* **api:** manual updates ([#67](https://github.com/terminaldotshop/terminal-sdk-python/issues/67)) ([3faef72](https://github.com/terminaldotshop/terminal-sdk-python/commit/3faef72e10292187a0e634668d36cb72ef4ee8c0))


### Chores

* **internal:** properly set __pydantic_private__ ([#64](https://github.com/terminaldotshop/terminal-sdk-python/issues/64)) ([479263c](https://github.com/terminaldotshop/terminal-sdk-python/commit/479263c3e932a14df5b7d5c1c67939103e7d2364))

## 0.1.0-alpha.11 (2025-02-25)

Full Changelog: [v0.1.0-alpha.10...v0.1.0-alpha.11](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.10...v0.1.0-alpha.11)

### Features

* **api:** manual updates ([#62](https://github.com/terminaldotshop/terminal-sdk-python/issues/62)) ([fe2bf41](https://github.com/terminaldotshop/terminal-sdk-python/commit/fe2bf41ae832f124045bc30eaf197e6e517fe76c))


### Chores

* **internal:** fix devcontainers setup ([#60](https://github.com/terminaldotshop/terminal-sdk-python/issues/60)) ([d347fb9](https://github.com/terminaldotshop/terminal-sdk-python/commit/d347fb968fa3cf1ef1a86c360cb22fd1b4907643))

## 0.1.0-alpha.10 (2025-02-21)

Full Changelog: [v0.1.0-alpha.9...v0.1.0-alpha.10](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.9...v0.1.0-alpha.10)

### Features

* **client:** allow passing `NotGiven` for body ([#57](https://github.com/terminaldotshop/terminal-sdk-python/issues/57)) ([9bedf28](https://github.com/terminaldotshop/terminal-sdk-python/commit/9bedf28a803840cbb645819dc4f982842e741ad8))


### Bug Fixes

* **client:** mark some request bodies as optional ([9bedf28](https://github.com/terminaldotshop/terminal-sdk-python/commit/9bedf28a803840cbb645819dc4f982842e741ad8))

## 0.1.0-alpha.9 (2025-02-17)

Full Changelog: [v0.1.0-alpha.8...v0.1.0-alpha.9](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.8...v0.1.0-alpha.9)

### Features

* **api:** manual updates ([#54](https://github.com/terminaldotshop/terminal-sdk-python/issues/54)) ([a998759](https://github.com/terminaldotshop/terminal-sdk-python/commit/a998759accdb5ff62736a0d6d0b67538e1f1fbb5))

## 0.1.0-alpha.8 (2025-02-16)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* **api:** manual updates ([#51](https://github.com/terminaldotshop/terminal-sdk-python/issues/51)) ([40ecc46](https://github.com/terminaldotshop/terminal-sdk-python/commit/40ecc46e0381d7313ae6e90a25811fd00d9b71fe))

## 0.1.0-alpha.7 (2025-02-16)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** manual updates ([#48](https://github.com/terminaldotshop/terminal-sdk-python/issues/48)) ([2aaa3a0](https://github.com/terminaldotshop/terminal-sdk-python/commit/2aaa3a0c02d8985c02a04e6f83bed212e924e5ca))

## 0.1.0-alpha.6 (2025-02-16)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** manual updates ([#45](https://github.com/terminaldotshop/terminal-sdk-python/issues/45)) ([578ba4a](https://github.com/terminaldotshop/terminal-sdk-python/commit/578ba4a0bb4d3f2cc985f5448cf1dbbe26c0a9ad))

## 0.1.0-alpha.5 (2025-02-14)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Bug Fixes

* asyncify on non-asyncio runtimes ([#42](https://github.com/terminaldotshop/terminal-sdk-python/issues/42)) ([f1aab42](https://github.com/terminaldotshop/terminal-sdk-python/commit/f1aab42c4b3e29719b499e4d8c3ed6c1a7a0c402))

## 0.1.0-alpha.4 (2025-02-07)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Chores

* **internal:** fix type traversing dictionary params ([#38](https://github.com/terminaldotshop/terminal-sdk-python/issues/38)) ([933f424](https://github.com/terminaldotshop/terminal-sdk-python/commit/933f4242cdbe5b24cc9245467619501067236240))
* **internal:** minor type handling changes ([#40](https://github.com/terminaldotshop/terminal-sdk-python/issues/40)) ([b201593](https://github.com/terminaldotshop/terminal-sdk-python/commit/b20159360a84cfb3caee540e16aeef3afe275bc9))

## 0.1.0-alpha.3 (2025-02-06)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** manual updates ([#36](https://github.com/terminaldotshop/terminal-sdk-python/issues/36)) ([28cbd5c](https://github.com/terminaldotshop/terminal-sdk-python/commit/28cbd5c3ef0152a8e44fe8b2dd7503e166cbc3f6))
* **client:** send `X-Stainless-Read-Timeout` header ([#35](https://github.com/terminaldotshop/terminal-sdk-python/issues/35)) ([0813596](https://github.com/terminaldotshop/terminal-sdk-python/commit/081359648af17a00df4c9c8dc940ad7f83fbd9c7))


### Chores

* **internal:** bummp ruff dependency ([#33](https://github.com/terminaldotshop/terminal-sdk-python/issues/33)) ([be260e9](https://github.com/terminaldotshop/terminal-sdk-python/commit/be260e9e9ec19b9f6b308d15a6f601360de68858))
* **internal:** change default timeout to an int ([#32](https://github.com/terminaldotshop/terminal-sdk-python/issues/32)) ([dd77511](https://github.com/terminaldotshop/terminal-sdk-python/commit/dd7751104d7be4702bff7fc9b20055b94c6b689d))

## 0.1.0-alpha.2 (2025-01-24)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** manual updates ([#15](https://github.com/terminaldotshop/terminal-sdk-python/issues/15)) ([c2cfede](https://github.com/terminaldotshop/terminal-sdk-python/commit/c2cfedeb1caed301de0a90cc31102de54944f24c))


### Bug Fixes

* correctly handle deserialising `cls` fields ([#24](https://github.com/terminaldotshop/terminal-sdk-python/issues/24)) ([d6100e9](https://github.com/terminaldotshop/terminal-sdk-python/commit/d6100e9247a36edbafca03732520d3df74b84831))
* **tests:** make test_get_platform less flaky ([#27](https://github.com/terminaldotshop/terminal-sdk-python/issues/27)) ([e3b092b](https://github.com/terminaldotshop/terminal-sdk-python/commit/e3b092b8a81f5cfc60d4e2f43f3fcd3ce3c05984))


### Chores

* add missing isclass check ([#19](https://github.com/terminaldotshop/terminal-sdk-python/issues/19)) ([bdbea91](https://github.com/terminaldotshop/terminal-sdk-python/commit/bdbea91f782a76ea2bf2d213dba5d5e97fb6a255))
* **internal:** avoid pytest-asyncio deprecation warning ([#28](https://github.com/terminaldotshop/terminal-sdk-python/issues/28)) ([18b476d](https://github.com/terminaldotshop/terminal-sdk-python/commit/18b476d7056299ae4531c5c63136df0db829f21c))
* **internal:** bump httpx dependency ([#20](https://github.com/terminaldotshop/terminal-sdk-python/issues/20)) ([daa15c9](https://github.com/terminaldotshop/terminal-sdk-python/commit/daa15c996b1b97cafbcfc44dc81a243047082fde))
* **internal:** codegen related update ([#17](https://github.com/terminaldotshop/terminal-sdk-python/issues/17)) ([9609704](https://github.com/terminaldotshop/terminal-sdk-python/commit/96097044ebbd3edd2b10addd71fe57ba7993e105))
* **internal:** codegen related update ([#18](https://github.com/terminaldotshop/terminal-sdk-python/issues/18)) ([ecd6805](https://github.com/terminaldotshop/terminal-sdk-python/commit/ecd6805a20139dedd33d89d162bdefc8f2b97aa1))
* **internal:** codegen related update ([#21](https://github.com/terminaldotshop/terminal-sdk-python/issues/21)) ([5ecf116](https://github.com/terminaldotshop/terminal-sdk-python/commit/5ecf1162ff0bf65c95b0510922d08c1c10f8de08))
* **internal:** codegen related update ([#23](https://github.com/terminaldotshop/terminal-sdk-python/issues/23)) ([28cdcd7](https://github.com/terminaldotshop/terminal-sdk-python/commit/28cdcd7e741f47fb457a31d9251ebb5fe6c3e245))
* **internal:** codegen related update ([#25](https://github.com/terminaldotshop/terminal-sdk-python/issues/25)) ([1544011](https://github.com/terminaldotshop/terminal-sdk-python/commit/1544011e2a206917111bc616add53fd96250ea11))
* **internal:** codegen related update ([#29](https://github.com/terminaldotshop/terminal-sdk-python/issues/29)) ([cdea992](https://github.com/terminaldotshop/terminal-sdk-python/commit/cdea9921bdee791449470c87456b739d551f6654))
* **internal:** minor formatting changes ([#30](https://github.com/terminaldotshop/terminal-sdk-python/issues/30)) ([a5022ec](https://github.com/terminaldotshop/terminal-sdk-python/commit/a5022ecb7a83b7ac0a35266e25f8bea64ef6b714))


### Documentation

* fix typos ([#22](https://github.com/terminaldotshop/terminal-sdk-python/issues/22)) ([1f2fc80](https://github.com/terminaldotshop/terminal-sdk-python/commit/1f2fc80f4cf35fb5e685e0c9c26c6cb48cbf86ac))
* **raw responses:** fix duplicate `the` ([#26](https://github.com/terminaldotshop/terminal-sdk-python/issues/26)) ([7c98ef0](https://github.com/terminaldotshop/terminal-sdk-python/commit/7c98ef0821cef4906866f8db84d4e1bd34b9bdce))

## 0.1.0-alpha.1 (2024-12-17)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/terminaldotshop/terminal-sdk-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** manual updates ([#10](https://github.com/terminaldotshop/terminal-sdk-python/issues/10)) ([03939b9](https://github.com/terminaldotshop/terminal-sdk-python/commit/03939b957d72737475bd8be906b320f7a5042261))
* **api:** manual updates ([#11](https://github.com/terminaldotshop/terminal-sdk-python/issues/11)) ([a938627](https://github.com/terminaldotshop/terminal-sdk-python/commit/a9386279808bcd6be93cc96ed76f8eb1338fbe0c))
* **api:** manual updates ([#3](https://github.com/terminaldotshop/terminal-sdk-python/issues/3)) ([8335371](https://github.com/terminaldotshop/terminal-sdk-python/commit/8335371af25183d8289a0c0773556632700c006d))
* **api:** manual updates ([#4](https://github.com/terminaldotshop/terminal-sdk-python/issues/4)) ([6fd1018](https://github.com/terminaldotshop/terminal-sdk-python/commit/6fd1018252bf39a468b0706a97b564f047784399))
* **api:** manual updates ([#5](https://github.com/terminaldotshop/terminal-sdk-python/issues/5)) ([a5a8295](https://github.com/terminaldotshop/terminal-sdk-python/commit/a5a8295366264f2b98c3dfa41ed59d1aba6921aa))
* **api:** manual updates ([#9](https://github.com/terminaldotshop/terminal-sdk-python/issues/9)) ([475486a](https://github.com/terminaldotshop/terminal-sdk-python/commit/475486a2b7b4e88a63283421e27b2cd1ca28874a))


### Chores

* configure new SDK language ([a118f7a](https://github.com/terminaldotshop/terminal-sdk-python/commit/a118f7aaf10faf0cf619b456c783d96e31f56759))
* go live ([#1](https://github.com/terminaldotshop/terminal-sdk-python/issues/1)) ([7f1ab32](https://github.com/terminaldotshop/terminal-sdk-python/commit/7f1ab32c1a034ad1e21bcc520a8a408de238dbd2))
* **internal:** codegen related update ([#6](https://github.com/terminaldotshop/terminal-sdk-python/issues/6)) ([4431189](https://github.com/terminaldotshop/terminal-sdk-python/commit/443118946e35803f0600ed8a4da45856c77d1690))
* **internal:** codegen related update ([#7](https://github.com/terminaldotshop/terminal-sdk-python/issues/7)) ([f6770fd](https://github.com/terminaldotshop/terminal-sdk-python/commit/f6770fdd861241670a280a8e30087103617b6428))


### Documentation

* **readme:** example snippet for client context manager ([#8](https://github.com/terminaldotshop/terminal-sdk-python/issues/8)) ([881d3e5](https://github.com/terminaldotshop/terminal-sdk-python/commit/881d3e586473b7fa94bf13805ecd3aac3a5f688e))
