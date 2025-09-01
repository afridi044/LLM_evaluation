# Rector Rules Analysis Report - Comprehensive

*Generated on 2025-08-31 05:42:37*

## Dataset Overview
- **Total Files Analyzed**: 100
- **Total Unique Rules Triggered**: 48
- **Total Rule Applications**: 521
- **PHP Versions Covered**: 18

# Top 20 Most Frequently Triggered Rector Rules

## Executive Summary
- **Total Unique Rules**: 48
- **Most Common Rule**: LongArrayToShortArrayRector (triggered in 88 files)
- **Analysis Date**: 2025-08-31 05:42:37

## Top 20 Rules by Frequency

| Rank | Rule Name | PHP Version | Files Affected | Avg File LOC | Total LOC Affected |
|------|-----------|-------------|----------------|--------------|-------------------|
| 1 | `LongArrayToShortArrayRector` | Php54 | 88 | 598 | 52607 |
| 2 | `NullToStrictStringFuncCallArgRector` | Php81 | 81 | 604 | 48894 |
| 3 | `TernaryToNullCoalescingRector` | Php70 | 49 | 735 | 36000 |
| 4 | `StrStartsWithRector` | Php80 | 32 | 859 | 27477 |
| 5 | `StrContainsRector` | Php80 | 30 | 745 | 22362 |
| 6 | `ListToArrayDestructRector` | Php71 | 29 | 832 | 24116 |
| 7 | `DirNameFileConstantToDirConstantRector` | Php53 | 27 | 389 | 10490 |
| 8 | `VarToPublicPropertyRector` | Php52 | 23 | 530 | 12193 |
| 9 | `ClassPropertyAssignToConstructorPromotionRector` | Php80 | 20 | 578 | 11560 |
| 10 | `FirstClassCallableRector` | Php81 | 13 | 717 | 9321 |
| 11 | `TernaryToElvisRector` | Php53 | 12 | 730 | 8755 |
| 12 | `ChangeSwitchToMatchRector` | Php80 | 12 | 1147 | 13767 |
| 13 | `CurlyToSquareBracketArrayStringRector` | Php74 | 9 | 1320 | 11878 |
| 14 | `Php4ConstructorRector` | Php70 | 8 | 666 | 5326 |
| 15 | `StringableForToStringRector` | Php80 | 8 | 341 | 2730 |
| 16 | `ClassOnObjectRector` | Php80 | 7 | 886 | 6200 |
| 17 | `AddOverrideAttributeToOverriddenMethodsRector` | Php83 | 7 | 570 | 3991 |
| 18 | `StrEndsWithRector` | Php80 | 6 | 1035 | 6209 |
| 19 | `ClassOnThisVariableObjectRector` | Php80 | 4 | 1154 | 4615 |
| 20 | `RemoveParentCallWithoutParentRector` | DeadCode | 4 | 599 | 2395 |

## PHP Version Migration Analysis

### Rule Distribution by PHP Version

| PHP Version | Files Affected | Unique Rules | Total Rule Triggers | Impact Level |
|-------------|----------------|--------------|-------------------|--------------|
| PHP 80 | 72 | 10 | 121 (23.2%) | 🔴 High |
| PHP 81 | 83 | 2 | 94 (18.0%) | 🟡 Medium |
| PHP 54 | 88 | 1 | 88 (16.9%) | 🟡 Medium |
| PHP 70 | 62 | 10 | 75 (14.4%) | 🟡 Medium |
| PHP 53 | 35 | 2 | 39 (7.5%) | 🟢 Low |
| PHP 71 | 30 | 3 | 31 (6.0%) | 🟢 Low |
| PHP 52 | 23 | 1 | 23 (4.4%) | 🟢 Low |
| PHP 74 | 12 | 3 | 13 (2.5%) | 🟢 Low |
| PHP 73 | 8 | 4 | 8 (1.5%) | 🟢 Low |
| PHP 83 | 7 | 1 | 7 (1.3%) | 🟢 Low |
| PHP 72 | 5 | 4 | 5 (1.0%) | 🟢 Low |
| DeadCode | 4 | 1 | 4 (0.8%) | 🟢 Low |
| PHP 56 | 3 | 1 | 3 (0.6%) | 🟢 Low |
| PHP 82 | 3 | 1 | 3 (0.6%) | 🟢 Low |
| TypeDeclaration | 3 | 1 | 3 (0.6%) | 🟢 Low |
| CodeQuality | 2 | 1 | 2 (0.4%) | 🟢 Low |
| PHP 55 | 1 | 1 | 1 (0.2%) | 🟢 Low |
| CodingStyle | 1 | 1 | 1 (0.2%) | 🟢 Low |

## Rule Category Analysis

### Most Common Rule Categories

| Category | Files Impacted | Unique Rules | Description |
|----------|-----------------|--------------|-------------|
| `FuncCall` | 89 | 16 | Function call transformations and modernizations |
| `Array_` | 88 | 2 | Array syntax and function improvements |
| `Ternary` | 55 | 2 | Ternary operator improvements |
| `Identical` | 33 | 2 | Code structure improvements |
| `NotIdentical` | 30 | 1 | Code structure improvements |
| `List_` | 29 | 1 | Code structure improvements |
| `Property` | 23 | 1 | Property declaration improvements |
| `Class_` | 20 | 3 | Class structure modifications |
| `ClassMethod` | 16 | 5 | Class method signature changes |
| `Switch_` | 12 | 1 | Code structure improvements |
| `ArrayDimFetch` | 9 | 1 | Code structure improvements |
| `Assign` | 4 | 2 | Assignment operator enhancements |
| `ClassConstFetch` | 4 | 1 | Code structure improvements |
| `StaticCall` | 4 | 1 | Code structure improvements |
| `ConstFetch` | 3 | 1 | Code structure improvements |
| `StmtsAwareInterface` | 3 | 1 | Code structure improvements |
| `Break_` | 2 | 1 | Code structure improvements |
| `MethodCall` | 2 | 1 | Code structure improvements |
| `While_` | 1 | 1 | Code structure improvements |
| `Closure` | 1 | 1 | Code structure improvements |
| `Variable` | 1 | 1 | Variable handling updates |
| `If_` | 1 | 1 | Conditional statement optimizations |
| `Catch_` | 1 | 1 | Code structure improvements |

## Migration Pattern Analysis

### Files Requiring Multi-Version Updates

| Pattern Type | File Count | Percentage | Migration Complexity |
|--------------|------------|------------|---------------------|
| Single PHP Version | 0 | 0.0% | 🟢 Simple |
| Multiple PHP Versions | 100 | 100.0% | 🔴 Complex |

### Most Common Version Combinations

- **PHP 54 + PHP 70 + PHP 80 + PHP 81**: 7 files
- **PHP 53 + PHP 54 + PHP 70 + PHP 80 + PHP 81**: 6 files
- **PHP 52 + PHP 80**: 6 files
- **PHP 53 + PHP 54 + PHP 81**: 5 files
- **PHP 54 + PHP 70 + PHP 71 + PHP 80 + PHP 81**: 4 files
- **PHP 53 + PHP 54 + PHP 70**: 4 files
- **PHP 54 + PHP 70 + PHP 71 + PHP 81**: 3 files
- **PHP 54 + PHP 70 + PHP 81**: 3 files
- **PHP 53 + PHP 54 + PHP 80 + PHP 81**: 3 files
- **DeadCode + PHP 52 + PHP 54 + PHP 70 + PHP 80 + PHP 81 + PHP 83**: 2 files


## File Complexity vs Migration Opportunities

### Rule Density by File Size

| File Size Category | Avg Rules per File | Avg PHP Versions | Avg LOC | Migration Density* |
|--------------------|-------------------|------------------|---------|------------------|
| Small (1-200) | 3.2 | 2.9 | 144 | 22.12 |
| Medium (201-500) | 5.4 | 4.8 | 350 | 15.41 |
| Large (501-1000) | 5.7 | 5.0 | 704 | 8.08 |
| Extra Large (1000+) | 8.9 | 6.2 | 1725 | 5.17 |

*Migration Density = Rules triggered per 1000 lines of code

### Key Insights
- **Larger files** tend to have more absolute migration opportunities
- **Smaller files** often have higher migration density (rules per LOC)
- **Medium files (201-500 LOC)** provide optimal balance for testing
- **Large files (501-1000 LOC)** offer substantial context for complex migrations


## Complete Rule Reference

### All Triggered Rules (Alphabetical)

| Rule Name | PHP Version | Files | Full Class Name |
|-----------|-------------|-------|-----------------|
| `AddOverrideAttributeToOverriddenMethodsRector` | Php83 | 7 | `Rector\Php83\Rector\ClassMethod\AddOverrideAttributeToOverriddenMethodsRector` |
| `ArrayKeyFirstLastRector` | Php73 | 1 | `Rector\Php73\Rector\FuncCall\ArrayKeyFirstLastRector` |
| `AssignArrayToStringRector` | Php71 | 1 | `Rector\Php71\Rector\Assign\AssignArrayToStringRector` |
| `BreakNotInLoopOrSwitchToReturnRector` | Php70 | 2 | `Rector\Php70\Rector\Break_\BreakNotInLoopOrSwitchToReturnRector` |
| `ChangeSwitchToMatchRector` | Php80 | 12 | `Rector\Php80\Rector\Switch_\ChangeSwitchToMatchRector` |
| `ClassConstantToSelfClassRector` | Php55 | 1 | `Rector\Php55\Rector\Class_\ClassConstantToSelfClassRector` |
| `ClassOnObjectRector` | Php80 | 7 | `Rector\Php80\Rector\FuncCall\ClassOnObjectRector` |
| `ClassOnThisVariableObjectRector` | Php80 | 4 | `Rector\Php80\Rector\ClassConstFetch\ClassOnThisVariableObjectRector` |
| `ClassPropertyAssignToConstructorPromotionRector` | Php80 | 20 | `Rector\Php80\Rector\Class_\ClassPropertyAssignToConstructorPromotionRector` |
| `ClosureToArrowFunctionRector` | Php74 | 1 | `Rector\Php74\Rector\Closure\ClosureToArrowFunctionRector` |
| `ConsistentImplodeRector` | CodingStyle | 1 | `Rector\CodingStyle\Rector\FuncCall\ConsistentImplodeRector` |
| `CreateFunctionToAnonymousFunctionRector` | Php72 | 2 | `Rector\Php72\Rector\FuncCall\CreateFunctionToAnonymousFunctionRector` |
| `CurlyToSquareBracketArrayStringRector` | Php74 | 9 | `Rector\Php74\Rector\ArrayDimFetch\CurlyToSquareBracketArrayStringRector` |
| `DirNameFileConstantToDirConstantRector` | Php53 | 27 | `Rector\Php53\Rector\FuncCall\DirNameFileConstantToDirConstantRector` |
| `EregToPregMatchRector` | Php70 | 4 | `Rector\Php70\Rector\FuncCall\EregToPregMatchRector` |
| `FinalPrivateToPrivateVisibilityRector` | Php80 | 1 | `Rector\Php80\Rector\ClassMethod\FinalPrivateToPrivateVisibilityRector` |
| `FirstClassCallableRector` | Php81 | 13 | `Rector\Php81\Rector\Array_\FirstClassCallableRector` |
| `IfIssetToCoalescingRector` | Php70 | 3 | `Rector\Php70\Rector\StmtsAwareInterface\IfIssetToCoalescingRector` |
| `IfToSpaceshipRector` | Php70 | 1 | `Rector\Php70\Rector\If_\IfToSpaceshipRector` |
| `ListToArrayDestructRector` | Php71 | 29 | `Rector\Php71\Rector\List_\ListToArrayDestructRector` |
| `LongArrayToShortArrayRector` | Php54 | 88 | `Rector\Php54\Rector\Array_\LongArrayToShortArrayRector` |
| `MultiDirnameRector` | Php70 | 4 | `Rector\Php70\Rector\FuncCall\MultiDirnameRector` |
| `NullCoalescingOperatorRector` | Php74 | 3 | `Rector\Php74\Rector\Assign\NullCoalescingOperatorRector` |
| `NullToStrictStringFuncCallArgRector` | Php81 | 81 | `Rector\Php81\Rector\FuncCall\NullToStrictStringFuncCallArgRector` |
| `OptionalParametersAfterRequiredRector` | CodeQuality | 2 | `Rector\CodeQuality\Rector\ClassMethod\OptionalParametersAfterRequiredRector` |
| `Php4ConstructorRector` | Php70 | 8 | `Rector\Php70\Rector\ClassMethod\Php4ConstructorRector` |
| `PowToExpRector` | Php56 | 3 | `Rector\Php56\Rector\FuncCall\PowToExpRector` |
| `RandomFunctionRector` | Php70 | 1 | `Rector\Php70\Rector\FuncCall\RandomFunctionRector` |
| `RemoveExtraParametersRector` | Php71 | 1 | `Rector\Php71\Rector\FuncCall\RemoveExtraParametersRector` |
| `RemoveParentCallWithoutParentRector` | DeadCode | 4 | `Rector\DeadCode\Rector\StaticCall\RemoveParentCallWithoutParentRector` |
| `RemoveUnusedVariableInCatchRector` | Php80 | 1 | `Rector\Php80\Rector\Catch_\RemoveUnusedVariableInCatchRector` |
| `ReturnNeverTypeRector` | TypeDeclaration | 3 | `Rector\TypeDeclaration\Rector\ClassMethod\ReturnNeverTypeRector` |
| `SensitiveConstantNameRector` | Php73 | 3 | `Rector\Php73\Rector\ConstFetch\SensitiveConstantNameRector` |
| `SetCookieRector` | Php73 | 1 | `Rector\Php73\Rector\FuncCall\SetCookieRector` |
| `StrContainsRector` | Php80 | 30 | `Rector\Php80\Rector\NotIdentical\StrContainsRector` |
| `StrEndsWithRector` | Php80 | 6 | `Rector\Php80\Rector\Identical\StrEndsWithRector` |
| `StrStartsWithRector` | Php80 | 32 | `Rector\Php80\Rector\Identical\StrStartsWithRector` |
| `StringableForToStringRector` | Php80 | 8 | `Rector\Php80\Rector\Class_\StringableForToStringRector` |
| `StringifyDefineRector` | Php72 | 1 | `Rector\Php72\Rector\FuncCall\StringifyDefineRector` |
| `StringifyStrNeedlesRector` | Php73 | 3 | `Rector\Php73\Rector\FuncCall\StringifyStrNeedlesRector` |
| `StringsAssertNakedRector` | Php72 | 1 | `Rector\Php72\Rector\FuncCall\StringsAssertNakedRector` |
| `TernaryToElvisRector` | Php53 | 12 | `Rector\Php53\Rector\Ternary\TernaryToElvisRector` |
| `TernaryToNullCoalescingRector` | Php70 | 49 | `Rector\Php70\Rector\Ternary\TernaryToNullCoalescingRector` |
| `ThisCallOnStaticMethodToStaticCallRector` | Php70 | 2 | `Rector\Php70\Rector\MethodCall\ThisCallOnStaticMethodToStaticCallRector` |
| `Utf8DecodeEncodeToMbConvertEncodingRector` | Php82 | 3 | `Rector\Php82\Rector\FuncCall\Utf8DecodeEncodeToMbConvertEncodingRector` |
| `VarToPublicPropertyRector` | Php52 | 23 | `Rector\Php52\Rector\Property\VarToPublicPropertyRector` |
| `WhileEachToForeachRector` | Php72 | 1 | `Rector\Php72\Rector\While_\WhileEachToForeachRector` |
| `WrapVariableVariableNameInCurlyBracesRector` | Php70 | 1 | `Rector\Php70\Rector\Variable\WrapVariableVariableNameInCurlyBracesRector` |